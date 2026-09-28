# Natural Chinese for Engineering Documents

The goal is restrained, readable technical Chinese.

## Sentence style

Prefer direct sentences such as:

> `cobot_id_start()` 先检查会话状态，再同步参数并清空目标批次。

Avoid padded versions such as:

> 值得注意的是，在整体实现过程中，`cobot_id_start()` 扮演着至关重要的角色，并首先进行一系列必要检查。

Use longer sentences only when the logical relationship benefits from staying together.

Mix short and medium-length paragraphs. Do not artificially alternate them.

## Transitions

Use explicit logical relationships when needed:

- 因此
- 但
- 这里
- 对应到代码
- 在这一阶段
- 与此不同
- 结果是

Do not add a transition at the start of every paragraph.

## Reduce stock AI phrasing

Avoid unnecessary repetition of:

- 值得注意的是
- 不难发现
- 显而易见
- 至关重要
- 尤为关键
- 从本质上讲
- 综上所述
- 总体而言
- 首先 / 其次 / 最后
- 不仅……而且……
- 这一设计有效地……
- 为后续……奠定坚实基础
- 具有重要意义

These phrases are not forbidden. Use them only when they carry real meaning.

## Avoid fake completeness

Do not force exactly three reasons, exactly five steps, a summary under every section, or an “advantages/future work” section.

Completeness comes from covering the engineering model, not from symmetrical formatting.

## Concrete language

Prefer verified identifiers, conditions, and quantities.

Example:

> `sample_count` 达到配置要求后，批次才进入完成判定。

is better than:

> 系统采集到足够的数据后会认为流程完成。

when the source provides the exact condition.

## Tone

Use neutral engineering tone.

Do not praise the design, dramatize normal implementation choices, address the reader repeatedly, write motivational filler, or imitate academic grandiosity.

## Headings

Headings should name the actual content.

Good:

- `3.2 J3/J4 力矩差模型`
- `5.1 为什么过渡段不参与采样`

Weak:

- `重要实现细节`
- `进一步讨论`
- `关键洞察`

## Bold and repetition

Use bold sparingly.
If a concept has already been explained, refer back to it rather than redefining it.
A final section should add synthesis, limitations, or next actions; it should not simply restate the introduction.
