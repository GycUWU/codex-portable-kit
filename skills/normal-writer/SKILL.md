---
name: normal-writer
description: Write, rewrite, review, or expand ordinary Chinese documents and long-form prose such as tutorials, manuals, reports, notices, operating guides, study notes, README-style documentation, and general explanations. Use for daily or non-robotics writing; use robotics-tech-writer for robotics, source-backed engineering, algorithms, or motion-control documentation.
---

# Normal Writer

## Core rule

For a substantial document, default to an outline before the full text. If the user explicitly requests the complete document or a different approval stage, follow that request.

Treat `确认`, `可以`, `按这个写`, `开始写正文`, `没问题`, `继续生成内容`, `use this outline`, and `proceed` as approval phrases.

For a short answer, message, title, translation, rewrite, or minor paragraph polish, answer directly without forcing the outline stage.

## Stage 1: outline

Write the outline atomically and in detail for a complete beginner. Break broad sections into small, independently understandable points; explicitly include prerequisites, terminology, transitions, examples, likely questions, and verification or practice steps. Do not assume the reader already knows the subject or silently group several teaching steps under one heading. The outline can be condensed after approval, but the initial planning outline should be exhaustive.

Include:

1. Document title.
2. Target reader.
3. Writing goal.
4. Assumptions and missing information.
5. Proposed section structure.
6. Key points under each section.
7. Useful examples, tables, diagrams, or code snippets.
8. Questions requiring confirmation.

For an explanatory document involving a process, result, problem, or “why”, include two complementary views when useful:

- Forward structure: purpose or input -> steps -> output.
- Reverse causal structure: output or observed phenomenon -> direct cause -> upstream mechanism -> root cause or supporting evidence.

Do not force the reverse view into short messages, notices, pure narratives, or content with no meaningful causal chain.

Use this format:

```markdown
# 大纲草案

## 1. 文档目标
...

## 2. 目标读者
...

## 3. 建议大纲
...

## 4. 需要你确认的问题
...

若本次任务未授权直接成文，请先审查这个大纲；用户确认后再生成完整正文。
```

After the outline, wait for approval only when the user has not already authorized full drafting. If the user asks to skip or combine stages, comply and keep the outline as brief planning context.

## Stage 2: full document

After approval, start with:

```markdown
# 正文
```

Follow the approved outline. When the outline includes both views, explain the forward path first and then use the reverse path to answer why the result occurs. Use clear, natural Chinese; explain unfamiliar terms before relying on them; prefer concrete examples; avoid empty claims, invented details, and unsupported certainty. Preserve the requested audience, tone, format, and section numbering.

End with:

```markdown
# 可继续完善的方向
```

List only practical, relevant improvements such as diagrams, examples, tables, screenshots, troubleshooting cases, or a shorter presentation version.
