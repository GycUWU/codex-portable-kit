# robotics-tech-writer

一个面向 Codex / ChatGPT 的中文工程技术文档 Skill。核心目标不是“把文字写得像人”，而是让模型先读懂源码和证据，再写出自然、准确、可维护的技术文档。

## 适用范围

适用于基于以下材料撰写文档：

- C/C++/Qt 等源码；
- 配置、XML、INI、Schema；
- 测试、日志、采样数据；
- 数学公式与算法实现；
- 项目内部已有说明。

尤其适合机器人、运动控制、EtherCAT、轨迹规划、运动学、负载辨识等工程软件。

## 安装到 Codex

### 仓库级

把整个目录复制到：

`.agents/skills/robotics-tech-writer`

建议放在仓库根目录的 `.agents/skills/` 下，便于项目成员共享。

### 用户级

把整个目录复制到：

`$HOME/.agents/skills/robotics-tech-writer`

如果修改后 Codex 没有立即显示，可重启 Codex。

## 调用

在 Codex CLI / IDE 中可显式使用：

`$robotics-tech-writer`

示例：

> 使用 `$robotics-tech-writer`。分析当前仓库 master 分支的 EndlessAxis 实现，先给出文档大纲。重点讲整体实现、关键数据结构、调用流程和边界处理，所有结论以源码为依据。

算法类：

> 使用 `$robotics-tech-writer`。阅读当前仓库 B 样条相关源码，解释弧长计算。先讲几何意义，再讲公式，最后逐一映射到代码变量。不要补充源码中不存在的算法。

Bug 类：

> 使用 `$robotics-tech-writer`。根据当前修改和日志写一份 Bug 修复说明，按照“现象→证据→根因→修改→验证”展开，把推断与事实分开。

## 可选风格检查

Markdown 文档生成后可以执行：

`python scripts/style_lint.py path/to/document.md`

它只给编辑建议，不代表技术正确性，也不应作为硬性评分器。

## 设计原则

写作顺序固定为：

`证据 -> 实现模型 -> 文档结构 -> 技术初稿 -> 技术审查 -> 中文润色 -> 最终检查`

“去 AI 味”被放在靠后阶段，防止为了语言自然而牺牲事实精度。
