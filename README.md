# Codex Portable Kit

[安装说明](Docs/INSTALL.md) · [Skills 清单](Docs/SKILLS.md) · [MCP 与插件](Docs/MCP-PLUGINS.md) · [许可证与来源](Docs/NOTICES.md)

本机 skills、MCP 和插件安装清单的迁移包。Skills 使用本地文件快照，安装时恢复目标用户路径；MCP 运行程序按依赖清单重新安装，账号授权在目标电脑重新完成。

让另一台 Codex 安装：

> 请读取这个仓库的 Docs/INSTALL.md，先校验迁移包，再安装全部 skills，恢复 FastCtx 和 Cloudflare MCP，安装外部插件和视频依赖，并按清单核验内置插件。保留目标电脑已有配置和账号授权。遇到需要登录的服务，请告知我具体服务和登录方法。

Windows 快速安装（先安装 Python 3.12、Node.js、Git 和 Codex 桌面应用）：

```powershell
git clone https://github.com/GycUWU/codex-portable-kit.git
cd codex-portable-kit
python scripts/verify.py
python scripts/install.py --mcp --plugins --preferences --video --runtimes
```

只安装 skills、不联网安装运行工具：`python scripts/install.py`。

包内有 76 个顶层 skill，另有 `video-use/skills/manim-video`。保留第三方许可证；`onetake`、`motion-web` 等有非商业用途限制，见各自 LICENSE。本仓库没有统一改变这些文件的许可证。
