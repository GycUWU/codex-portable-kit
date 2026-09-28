---
name: write
description: Route Chinese writing requests to the appropriate writing Skill. Use when the user invokes `$write`, asks Codex to write without naming a specialized writer, or when the task may be either robotics/technical documentation or ordinary Chinese writing.
---

# Write Router

Use `write` as the stable entry point, then delegate the actual writing workflow to exactly one specialized Skill.

## Routing rules

Route to `robotics-tech-writer` when the request is about robotics, motion control, EtherCAT, trajectory planning, kinematics, payload identification, C/C++/Qt implementation, algorithms, source-code behavior, logs, formulas, configuration, or a bug/fix record grounded in engineering evidence.

Route to `normal-writer` for daily or general Chinese writing, including notices, tutorials, manuals, reports, operating guides, README-style documents, study notes, summaries, and ordinary long-form prose that is not robotics/source-backed engineering documentation.

When a request contains both kinds of content, route to `robotics-tech-writer` if the central claims must be verified against implementation, formulas, logs, or robotics/control behavior; otherwise route to `normal-writer`.

## Delegation protocol

1. State the selected Skill and the one-sentence reason when the distinction is not obvious.
2. Load and follow only the selected Skill's workflow; do not merge two writing templates.
3. Preserve the user's requested audience, format, language, and approval stage.
4. If the user explicitly names `$robotics-tech-writer` or `$normal-writer`, honor that explicit choice unless it is impossible for the supplied sources.

## Outline granularity

When the selected writing workflow requires an outline, use an atomic, exhaustive outline: split the document into small, independently understandable points, explain what each point will answer or accomplish, and assume the reader is a complete beginner. Do not hide prerequisite concepts, transitions, terms, decisions, examples, or verification steps inside a broad heading. The outline may be compressed later for presentation, but the planning version should be deliberately detailed.

## Do not draft here

This router only classifies and delegates. It should not duplicate the full drafting rules of either specialized Skill.
