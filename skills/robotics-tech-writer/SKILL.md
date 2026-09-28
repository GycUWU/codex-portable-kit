---
name: robotics-tech-writer
description: Write, rewrite, review, or expand Chinese engineering documentation grounded in source code, configuration, tests, logs, formulas, and user-provided technical sources. Use for robotics, motion control, C/C++/Qt, algorithms, EtherCAT, trajectory planning, payload identification, kinematics, bug analysis, implementation notes, architecture explanations, and similar code-backed technical documents. Do not use for coding-only tasks, marketing copy, fiction, or generic prose with no technical-document deliverable.
---

# Robotics Technical Writer

Produce engineering documentation that reads like it was written by an engineer who actually inspected the implementation.

Priority order:

1. Technical truth.
2. Traceability to sources.
3. Clear mental model.
4. Useful structure.
5. Natural Chinese.
6. Visual polish.

Never improve style by weakening technical precision.

## Operating principle

Do not start by drafting prose. First establish what the implementation actually does.

For source-backed tasks, inspect the relevant repository files, configuration, tests, logs, schemas, comments, call sites, and existing documentation before writing claims about behavior.

If a claim cannot be verified from available sources, omit it, mark it as an inference, or explicitly state that the current sources do not establish it.

Never invent function behavior, parameter meaning, units, timing guarantees, performance figures, state transitions, formulas, historical reasons, or design intent.

## Workflow

### 1. Resolve the document goal

Determine the requested document type:

- feature implementation explanation,
- algorithm explanation,
- architecture/module overview,
- bug analysis and fix record,
- API or usage guide,
- learning note based on code,
- technical report section,
- existing-document rewrite.

Determine the intended reader from context. Default to an engineer who knows basic programming but is unfamiliar with this module.

If the user already supplied scope, format, audience, branch, or source constraints, preserve them. Do not ask again.

### 2. Build a source inventory

Before drafting, identify the evidence available:

- source files,
- headers and data structures,
- configuration files,
- tests,
- logs,
- diagrams,
- PDFs or specifications,
- Git history or issue context when available,
- user-provided facts and corrections.

Use `references/source-grounding.md`.

For code-backed documentation, locate the implementation rather than relying on filenames alone.

### 3. Build the implementation model

Create an internal map of:

- entry points,
- important structures and state,
- call chain,
- data flow,
- control flow,
- inputs and outputs,
- initialization and teardown,
- error paths,
- boundary conditions,
- relevant formulas,
- configuration dependencies.

Do not expose an oversized inventory in the final document unless useful to the reader.

When a feature spans multiple files, explain the relationship before drilling into individual functions.

### 4. Select the document structure

Choose a structure from `references/document-structures.md`.

Do not force every document into the same template.

When presenting an outline for approval, make it atomic and exhaustive for a beginner reader. Break each broad section into small, independently understandable points, and explicitly list prerequisites, terminology, data or control transitions, examples, edge cases, and validation steps. Do not assume the reader knows the robotics domain, project architecture, or implementation vocabulary. The outline may be condensed in the final document after approval, but the planning outline should expose the complete learning path.

Prefer a progression such as:

`problem / purpose -> principle -> architecture -> implementation -> runtime flow -> edge cases -> validation`

when that progression matches the subject.

For call flows, architecture, algorithms, validation results, and bug or behavior explanations, add a reverse causal view when it helps the reader understand why the result occurs. Show both:

- Forward implementation tree: entry point -> stages/functions -> data or control flow -> output.
- Reverse causal tree: final output or observed issue -> immediate prerequisite/cause -> upstream stage or mechanism -> root cause and evidence.

The reverse tree is a causal trace, not a mechanically reversed list. Start from the result or phenomenon and ask “what had to be obtained or true before this could happen?” Stop when the available source no longer supports a claim.

For algorithm-heavy topics, load `references/algorithm-explanation.md`.
For code implementation, load `references/code-documentation.md`.
For bug analysis, load `references/bug-analysis.md`.

### 5. Draft from evidence

Write the first draft for technical completeness.

Rules:

- Explain why a mechanism exists before listing implementation details when the reason is known.
- When the document explains a result or phenomenon, use the reverse causal view to connect that result back to the responsible mechanism and evidence.
- Introduce a structure or function only when it contributes to the story.
- Define symbols, units, coordinate conventions, states, and abbreviations at first meaningful use.
- Keep code snippets short and directly relevant.
- Distinguish source code from pseudocode.
- Distinguish observed behavior from intended behavior.
- Distinguish facts from inference.
- Preserve the exact terminology used by the project unless the user asks for normalization.
- If terminology is inconsistent in the source, mention the inconsistency rather than silently rewriting the system.

### 6. Explain algorithms at three levels

When an algorithm is central, explain it in this order where applicable:

1. Physical or geometric intuition.
2. Mathematical model.
3. Code realization.

Connect formulas to concrete variables and functions in the implementation.

For each important formula, state:

- what problem it solves,
- variable meanings,
- units or dimensions when relevant,
- assumptions,
- where the inputs come from,
- where the result is used.

Do not dump formulas without connecting them to execution.

### 7. Review technical integrity

Before stylistic editing, check:

- Is every important behavior supported?
- Are function names, field names, indices, constants, units, and state names accurate?
- Did the document confuse command values with feedback values?
- Did it confuse coordinate frames?
- Did it confuse mathematical variables with code variables?
- Did it infer intent from a name or comment without corroboration?
- Are exceptional paths described where they change behavior?
- Are diagrams/tables consistent with the implementation?
- Are quoted code fragments exact?

Use `references/review-checklist.md`.

### 8. Humanize the Chinese

Only after technical review, edit the prose with `references/human-writing-zh.md`.

The objective is natural engineering Chinese, not casual chat.

Do not optimize for AI-detector evasion.

Prefer concrete nouns and verbs, varied but controlled sentence length, direct transitions, and explanations attached to actual implementation details.

Avoid mechanical habits such as:

- every section starting with background filler,
- repeated “首先 / 其次 / 最后”,
- repeated “值得注意的是”,
- repeated “综上所述”,
- empty claims such as “至关重要” without evidence,
- formulaic “不仅……而且/更……”,
- excessive bold text,
- one table per section,
- summary paragraphs that merely repeat the preceding paragraph,
- three-item lists used only because three sounds complete,
- identical paragraph length across the document.

Do not remove a phrase merely because it appears on an AI-style watchlist when it is genuinely the clearest wording.

### 9. Run the style lint when practical

For Markdown output saved to a file, optionally run:

`python scripts/style_lint.py <document.md>`

Treat the output as editorial warnings, not correctness errors.

Never change a technically correct sentence solely to make the lint score lower.

### 10. Final reader check

Ask:

- Can a new engineer explain the module after reading this?
- Can they trace a concept from principle to code?
- Can they tell which file/function to inspect next?
- Can they reproduce the described runtime flow?
- Can they see uncertainty where the source is incomplete?
- Does the document contain material that helps the reader act, debug, modify, or learn?

Delete filler that fails this test.

## Source priority

When sources conflict, use this default priority unless the task defines another:

1. Explicit user corrections and task-specific requirements.
2. Current implementation and configuration actually used by the target branch/build.
3. Tests and observed logs that demonstrate behavior.
4. Project-local technical documentation.
5. Upstream or vendor documentation.
6. Comments.
7. Naming-based inference.

A comment is evidence, but it is not stronger than executable behavior.

If a source is stale or branch-specific, say so.

## Tables

Use tables for genuine comparison or mapping, such as:

- UI field -> code field -> meaning,
- object index -> name -> data type,
- state -> transition condition -> action,
- before -> bug -> after,
- symbol -> code variable -> unit.

Do not use a table merely to make a page look organized.

## Code excerpts

When quoting source code:

- preserve identifiers exactly,
- include only enough surrounding context to understand the point,
- explain the code after or before the snippet,
- avoid line-by-line paraphrase of obvious syntax.

If code is reconstructed or simplified, label it as pseudocode or simplified logic.

## Diagrams

When a diagram would materially improve understanding, prefer diagrams that reveal call flow, state transition, data flow, coordinate relationship, geometric construction, timing relationship, or memory/PDO mapping.

Do not create decorative diagrams that add no information.

## Output discipline

Default to a finished document, not commentary about how to write one.

If the user asks for an outline first, provide only the outline until they approve or ask to continue.

If the user asks to write in stages, maintain terminology and section numbering across stages.

If asked to update an existing document, preserve unaffected content and change only what the evidence supports.

If the available source is insufficient, state exactly what is missing and write only the supported portion.

## Reference loading

Load these only when relevant:

- `references/source-grounding.md` — evidence and uncertainty rules.
- `references/document-structures.md` — document templates by task type.
- `references/code-documentation.md` — implementation explanation.
- `references/algorithm-explanation.md` — math/geometry/algorithm explanation.
- `references/bug-analysis.md` — bug and fix documentation.
- `references/human-writing-zh.md` — natural Chinese editing.
- `references/review-checklist.md` — final QA.
- `references/robotics-terminology.md` — robotics/control terminology conventions.

Use `assets/technical-document-template.md` as a starting scaffold only when it fits the task.
