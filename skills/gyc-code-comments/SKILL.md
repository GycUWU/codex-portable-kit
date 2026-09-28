---
name: gyc-code-comments
description: Review, add, rewrite, or clean up source-code comments so they explain intent, constraints, algorithms, bug fixes, and engineering rationale without restating obvious code. Use when Codex is modifying existing code, fixing bugs, adding features, improving comments, documenting C/C++ APIs with Doxygen, explaining algorithms or formulas, working on robotics/motion-control code, documenting realtime/concurrency behavior, or normalizing TODO/FIXME comments. When bug fixes, feature additions, or meaningful changes are made to existing code, apply the project's gyc author/date change-marking convention.
---

# Code Comment Quality

Improve comments without turning source code into prose.

The goal is to preserve information that is difficult to infer from code alone:

- why the code exists,
- what engineering constraint it satisfies,
- what assumption it relies on,
- what failure it prevents,
- how formulas map to implementation,
- what coordinate frame, unit, sign convention, state, or concurrency rule applies,
- who introduced a meaningful change and when, when project change-marking requires it.

## Core workflow

1. Read the surrounding implementation before editing comments.
2. Identify the code's real intent, data flow, state assumptions, error paths, units, and invariants.
3. Preserve correct existing project terminology and comment style.
4. Delete or rewrite comments that merely translate syntax into natural language.
5. Add comments only where they provide information not obvious from the code.
6. When modifying existing code for a feature, bug fix, or meaningful behavior change, apply the gyc change-marking rules in `references/general-comments.md`.
7. Check every edited comment against the final code so no stale explanation remains.
8. For nontrivial comments in a modular codebase, identify the owning module before the detailed explanation. Use the format `模块：详细说明`; for example, `去重：统一使用归一化X和Y计算匹配score，避免同一工件重复入队`.

## Load references conditionally

Read `references/general-comments.md` for all comment-writing or comment-review tasks. It also defines the required gyc author/date change-marking convention.

Read `references/cpp-doxygen.md` when documenting C/C++ public functions, headers, structs, classes, enums, callbacks, or APIs.

Read `references/algorithms-math.md` when code contains equations, numerical methods, filtering, optimization, interpolation, fitting, kinematics, dynamics, estimation, or other nontrivial algorithms.

Read `references/robotics-control.md` when code involves robots, joints, Cartesian motion, coordinate frames, trajectories, control, calibration, payload identification, drives, IO, EtherCAT, or similar automation logic.

Read `references/realtime-concurrency.md` when code involves threads, realtime loops, atomics, memory barriers, lock-free state, shared buffers, callbacks, producer/consumer logic, or timing constraints.

Read `references/todo-fixme.md` when adding, cleaning, or reviewing TODO, FIXME, HACK, NOTE, PERF, REVIEW, or similar markers.

## Comment priority

Prefer comments that explain:

1. WHY the logic is required.
2. Hidden constraints and invariants.
3. Failure modes and boundary conditions.
4. Units, coordinate frames, sign conventions, and reference definitions.
5. Algorithmic reasoning that is not obvious from the implementation.
6. Protocol, hardware, or external-system assumptions.
7. Important performance, realtime, or concurrency constraints.

Avoid comments that only explain WHAT a readable line already does.

## Modular comment convention

When a comment explains a meaningful algorithm, behavior change, boundary condition, or engineering constraint, prefix the explanation with its primary module name. The module prefix is concise Chinese text followed by a full-width colon, such as `去重：`、`排序：`、`传送带：`、`姿态：`、`涂胶：`、`通讯：`、`触发：` or `队列：`.

For gyc change markers, keep the author/date marker first and put the module prefix immediately after the marker:

```cpp
// modified by gyc 2026-08-15：去重：使用归一化X和Y计算综合匹配分数
```

For a multi-line changed block:

```cpp
// modified by gyc 2026-08-15 start：去重：未匹配点先进入候选缓存，避免单帧测量漂移造成重复入队
...
// modified by gyc 2026-08-15 end
```

Use the most specific primary module that owns the decision. Do not add multiple module labels merely for consistency, and do not rewrite unrelated historical comments only to add a prefix. Trivial comments and comments that only describe obvious syntax do not need a module prefix.

## Preserve source quality

Do not:

- rewrite unrelated code just to make comments look uniform,
- reformat large areas unless required by the task,
- invent bug IDs, requirement IDs, units, coordinate frames, algorithm names, or hardware behavior,
- infer a technical reason and present it as fact when the code or user context does not support it,
- change another engineer's author/date markers unless the user explicitly requests it,
- remove historical markers that still delimit active project code,
- attach gyc markers to formatting-only or behavior-neutral edits.
- normalize line endings as a side effect of a targeted edit; preserve the file's existing encoding and CRLF/LF style, and restore it before review if a tool converted CRLF to LF so Git does not report the whole file as changed.

When intent is uncertain, keep the comment factual and limited to what the implementation proves.

## Final review

Before finishing:

- verify comments match the final code,
- remove duplicated explanation,
- ensure modification markers cover only the actual changed lines,
- ensure single-line changes do not use `start/end`,
- ensure multi-line marked blocks have matching `start/end`,
- verify author is `gyc`,
- verify date uses the actual modification date in `YYYY-MM-DD` format,
- verify the marker comes first and the explanation follows a full-width colon; for a multi-line start marker, place `start` before the colon, while the end marker stays short,
- keep comments concise enough to scan during code review.
