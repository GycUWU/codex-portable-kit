# 安装与验收

## 操作顺序

1. 在目标电脑克隆此仓库，确认使用 Python 3.12 与 Node.js。Windows 使用 `python` 或 `py -3`，不依赖商店占位的 `python3` 命令。
2. 运行 `python scripts/verify.py`。文件哈希不匹配时停止安装，重新下载仓库。
3. 只迁移技能：`python scripts/install.py`。完整迁移：`python scripts/install.py --mcp --plugins --preferences --video --runtimes`。
4. `--mcp` 安装 FastCtx 的平台程序，并添加 FastCtx、Cloudflare 配置。先保留已有同名配置；不要把当前电脑的 `.codex/config.toml` 整份覆盖到目标电脑。
5. `--plugins` 恢复 ponytail、i-have-adhd 的 Git 插件市场及插件。按 MCP-PLUGINS.md 核对桌面应用中的内置插件。
6. `--preferences` 只创建缺失的 AGENTS.md 和通用偏好文件，保留已有文件。这里没有个人项目的历史记忆。
7. `--video` 安装 onetake 的 Python 工具链与 Chromium；Windows 在缺少 FFmpeg 时用 WinGet 安装。语音转录、语音合成、CUDA、Manim、Remotion 项目依赖按对应 skill 任务另行安装。
8. `--runtimes` 同时安装已盘点到的 context-mode 运行包；此机当前没有独立的 context-mode MCP 配置，因此安装器也不自动启用该服务器。需要使用其 ctx_* 工具时，用 `codex mcp add context-mode -- node <目标用户目录>/.codex/migration-tools/node_modules/context-mode/cli.bundle.mjs` 配置并验收。

安装前先检查目标电脑的权限。写入用户目录、安装依赖、访问 npm/PyPI/GitHub 被当前 Codex 环境限制时，申请对应权限；不要把权限失败当成安装完成。

## 保留与备份

安装目录为 `~/.agents/skills`。覆盖已有不同文件前，在 `~/.codex/migration-backups/<时间>/` 保存旧文件；不删除已有的额外文件。`--home <绝对目录>` 可用于隔离测试。

`{{HOME_POSIX}}`、`{{HOME_WIN}}`、`{{HOME_WIN_ESCAPED}}` 在安装时转换为目标用户目录。其他磁盘和工程路径保留原文，需要按实际项目调整。部分 skill 专用于 Windows 或特定工具，macOS/Linux 上需按其文档补齐对应环境。

同名 skill 的 `.codex` 差异版本在 `variants/`；安装默认使用 `skills/`。这些差异不自动覆盖默认版本。

## 验收标准

- `python scripts/verify.py` 通过，76 个顶层目录均包含 SKILL.md，嵌套 Manim 文件存在。
- `codex mcp list` 能列出 FastCtx 与 Cloudflare；FastCtx 在新任务能调用 read/grep/glob。
- `codex mcp login cloudflare-api` 完成该电脑的 OAuth 授权。GitHub、Notion 等账号连接也在目标电脑重新连接。
- 内置插件清单逐项核对；不可用项明确记录，不能仅复制 enabled 字段后宣称安装完成。
- 视频环境运行 `python -m pip check`、`node ~/.agents/skills/onetake/scripts/test_motion.js`；检查 ffmpeg、ffprobe 版本与 Chromium 启动。
- 重新打开 Codex/终端刷新新 PATH，下一轮任务确认 skills 出现在可用列表。

## 代理与重新连接

只提供 `config/proxy.env.example`，不自动设置代理。按目标电脑代理端口填写；没有监听的代理端口会导致连接失败。旧电脑的 `.env`、浏览器管道 ID、桌面 node_repl 二进制路径与账号令牌均不迁移。

官方安装与配置规则：[Skills](https://learn.chatgpt.com/docs/build-skills)、[MCP](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)。
