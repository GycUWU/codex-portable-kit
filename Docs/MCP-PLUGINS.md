# MCP 与插件清单

MCP = Codex 调用外部工具的连接配置；skill = 指导 Codex 何时、如何使用工具的工作流程。

## 本机直接配置的 MCP

| 服务 | 迁移方式 | 新电脑需要完成的事项 |
|---|---|---|
| fastctx | 通过 npm fastctx 0.2.6 安装目标平台程序 | 当前配置原先调用 0.1.1 原生二进制；迁移使用本机已有 npm 发行版 0.2.6，不复制旧二进制 |
| cloudflare-api | https://mcp.cloudflare.com/mcp | 执行 codex mcp login cloudflare-api，重新 OAuth 授权 |
| node_repl | 桌面 computer-use 插件生成 | 让目标 Codex 生成自己的运行时和浏览器管道，不复制本机生成配置 |

FastCtx 的 token budget 保存在 manifest.json 中，安装器恢复对应环境变量。context-mode 1.0.169 是已安装的 npm 工具，但不在当前显式 MCP 配置中，故默认只恢复包、不添加服务。

## 当前启用的插件

| 来源 | 插件 |
|---|---|
| openai-primary-runtime | documents、spreadsheets、presentations、pdf、template-creator |
| openai-bundled | visualize、codex-app-tools、browser、unified-computer-use、chrome、computer-use |
| 外部 Git 市场 | ponytail@ponytail、i-have-adhd@i-have-adhd |

外部市场：https://github.com/DietrichGebert/ponytail.git 和 https://github.com/ayghri/i-have-adhd.git。`--plugins` 用 Codex CLI 添加市场及插件。

内置市场由目标 Codex 桌面应用安装，避免复制旧电脑的缓存、运行时和内部路径；缺失时在插件库安装同名插件，或在已配置相应市场的情况下用 `codex plugin add 插件名@市场名`。桌面插件的版本可能随应用更新，不承诺与源电脑二进制完全一致。

## 账号连接与应用能力

GitHub、Notion、Sites 等连接由当前宿主提供，并不是 skills 文件。GitHub 等 OAuth、浏览器扩展授权、Cloudflare 登录需要重新连接；web、image_gen、应用管理等内置工具由新电脑的 Codex/账号提供，不能通过此 Git 仓库复制。

本机其他 npm CLI 的版本仅在 manifest.json 登记：Claude Code、Gemini CLI、DevSpace。这些是独立应用，不自动安装。

当前会话可调用的工具名称另存为 `inventory/session-tools.json`，用于目标 Codex 对照账号连接和宿主工具，清单本身不授予工具调用能力。
