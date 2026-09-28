"""迁移包校验：完整性、路径边界和常见凭据格式。"""
from pathlib import Path
import hashlib
import json
import re

SECRET = re.compile(rb"gh[pousr]_[A-Za-z0-9]{25,}|github_pat_[A-Za-z0-9_]{30,}|sk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{25,}|AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_-]{30,}|xox[baprs]-[A-Za-z0-9-]{20,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|eyJ[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{15,}")


def safe(root, relative):
    """added by gyc 2026-09-28：边界：拒绝绝对路径和越过包根目录的路径。"""
    rel = Path(relative)
    if rel.is_absolute() or rel.drive or ".." in rel.parts:
        raise ValueError(f"路径越界：{relative}")
    path = (root / rel).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError(f"路径越界：{relative}")
    return path


def check(root):
    sums = json.loads((root / "checksums.json").read_text(encoding="utf-8"))
    for rel, expected in sums.items():
        p = safe(root, rel)
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != expected:
            raise ValueError(f"完整性校验失败：{rel}")
    for p in root.rglob("*"):
        if not p.is_file() or any(x in {".git", "__pycache__", ".test-output"} for x in p.relative_to(root).parts):
            continue
        rel = p.relative_to(root).as_posix()
        if rel != "checksums.json" and rel not in sums:
            raise ValueError(f"发现未登记文件：{rel}")
        if p.name in {".env", "auth.json", "credentials.json", ".credentials.json", "cookies.json"}:
            raise ValueError(f"发现不应发布的文件：{p.relative_to(root)}")
        if p.suffix.lower() not in {".png", ".jpg", ".gif", ".mp4", ".wav", ".ttf", ".woff", ".woff2", ".zip"} and SECRET.search(p.read_bytes()):
            raise ValueError(f"发现疑似凭据：{p.relative_to(root)}")
    return len(sums)


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    print(f"校验通过：{check(root)} 个文件；常见凭据扫描通过。")
