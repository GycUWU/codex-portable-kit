"""安装技能快照，可选恢复 MCP、插件、偏好和视频依赖。"""
from pathlib import Path
import argparse
import datetime
import json
import os
import shutil
import subprocess
import sys
from verify import check, safe

ROOT = Path(__file__).resolve().parents[1]


def expand(data, home):
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return data
    replacements = {"{{HOME_WIN_ESCAPED}}": str(home).replace("\\", "\\\\"),
                    "{{HOME_WIN}}": str(home), "{{HOME_POSIX}}": home.as_posix()}
    for token, value in replacements.items():
        text = text.replace(token, value)
    return text.encode("utf-8")


def put(src, dst, home, backup):
    """added by gyc 2026-09-28：备份：覆盖不同内容前留存原文件，不删除目标目录的其他文件。"""
    if not dst.resolve().is_relative_to(home) or not backup.resolve().is_relative_to(home):
        raise ValueError("目标文件或备份目录通过链接越过用户目录")
    data = expand(src.read_bytes(), home)
    if dst.exists():
        if dst.read_bytes() == data:
            return
        old = backup / dst.relative_to(home)
        old.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(dst, old)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(data)


def run(args, capture=False):
    result = subprocess.run([str(x) for x in args], check=False, capture_output=capture, text=capture, encoding="utf-8" if capture else None)
    if result.returncode:
        raise RuntimeError(f"命令执行失败（{result.returncode}）：{Path(str(args[0])).name}")
    return result.stdout.strip() if capture else None


def command(name):
    executable = shutil.which(name)
    if not executable:
        raise RuntimeError(f"缺少命令：{name}，请先安装并重新打开终端。")
    return executable


def tools(home, manifest, context=False):
    prefix = safe(home, ".codex/migration-tools")
    packages = [f"fastctx@{manifest['npm_packages']['fastctx']['version']}"]
    if context:
        packages.append(f"context-mode@{manifest['npm_packages']['context-mode']['version']}")
    if not shutil.which("codex"):
        packages.append(f"@openai/codex@{manifest['npm_packages']['@openai/codex']['version']}")
    run([command("npm"), "install", "--prefix", prefix, "--save-exact", *packages])
    node = command("node")
    cli = [shutil.which("codex")] if shutil.which("codex") else [node, prefix / "node_modules/@openai/codex/bin/codex.js"]
    return node, prefix / "node_modules", cli


def restore_mcp(cli, node, modules, manifest):
    # added by gyc 2026-09-28：MCP：保留目标电脑已有同名配置及其账号授权。
    listed = json.loads(run([*cli, "mcp", "list", "--json"], capture=True))
    existing = {s['name'] for s in listed}
    if "fastctx" not in existing:
        env = []
        for key, value in manifest['mcp'][0]['env'].items():
            env.extend(["--env", f"{key}={value}"])
        run([*cli, "mcp", "add", "fastctx", *env, "--", node, modules / "fastctx/launcher.js", "serve"])
    if "cloudflare-api" not in existing:
        run([*cli, "mcp", "add", "cloudflare-api", "--url", "https://mcp.cloudflare.com/mcp"])
    print("MCP 配置已恢复；Cloudflare 需在目标电脑重新登录，桌面 node_repl 由应用生成。")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--home", type=Path, default=Path.home(), help="目标用户主目录；测试可指定临时目录")
    for flag in ["mcp", "plugins", "preferences", "video", "runtimes"]:
        parser.add_argument("--" + flag, action="store_true")
    args = parser.parse_args()
    if not args.home.is_absolute():
        parser.error("--home 必须使用绝对路径")
    home = args.home.resolve()
    # added by gyc 2026-09-28：校验：所有负载在写入目标电脑之前统一检查。
    check(ROOT)
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    backup = home / ".codex/migration-backups" / datetime.datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    for record in manifest['skills']:
        source = safe(ROOT / "skills", record['directory'])
        for p in source.rglob("*"):
            if p.is_file():
                target = safe(home / ".agents/skills", f"{record['directory']}/{p.relative_to(source).as_posix()}")
                put(p, target, home, backup)
    print(f"已安装 {len(manifest['skills'])} 个顶层 skill：{home / '.agents/skills'}")
    if args.preferences:
        for p in (ROOT / "config/memories").glob("*.md"):
            target = home / ".codex/memories" / p.name
            if not target.exists():
                put(p, target, home, backup)
        target = home / ".codex/AGENTS.md"
        if not target.exists():
            put(ROOT / "config/AGENTS.md.template", target, home, backup)
        print("偏好模板已安装；已有 AGENTS.md 和记忆文件保留。")
    if args.mcp or args.plugins or args.runtimes:
        node, modules, cli = tools(home, manifest, context=args.runtimes)
        env = os.environ.copy()
        # --home 同时决定 Codex CLI 配置位置，便于隔离测试与多用户迁移。
        os.environ['CODEX_HOME'] = str(home / ".codex")
        try:
            if args.mcp:
                restore_mcp(cli, node, modules, manifest)
            if args.plugins:
                for name, source in manifest['marketplaces'].items():
                    ref = source.get('last_revision') or source.get('ref')
                    extra = ["--ref", ref] if ref else []
                    run([*cli, "plugin", "marketplace", "add", source['source'], *extra])
                    run([*cli, "plugin", "add", f"{name}@{name}"])
                print("外部插件已恢复；OpenAI 内置插件请按 Docs/MCP-PLUGINS.md 的清单在桌面应用中启用。")
        finally:
            if 'CODEX_HOME' in env:
                os.environ['CODEX_HOME'] = env['CODEX_HOME']
            else:
                os.environ.pop('CODEX_HOME', None)
    if args.video:
        run([sys.executable, "-m", "pip", "install", "-r", ROOT / "Dependencies/video-requirements.txt"])
        run([sys.executable, "-m", "playwright", "install", "chromium"])
        if not (shutil.which("ffmpeg") and shutil.which("ffprobe")):
            if sys.platform != "win32":
                raise RuntimeError("请用系统包管理器安装 FFmpeg/ffprobe，再重新运行 --video。")
            run([command("winget"), "install", "--id", "Gyan.FFmpeg.Shared", "--exact", "--scope", "user", "--accept-package-agreements", "--accept-source-agreements"])
            print("FFmpeg 已安装；重新打开终端/Codex 以刷新 PATH。")
    print("安装完成；skills 会在 Codex 下一轮任务加载。")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, RuntimeError, json.JSONDecodeError) as error:
        sys.exit(str(error))
