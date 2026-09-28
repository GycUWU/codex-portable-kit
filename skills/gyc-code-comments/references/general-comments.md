# General Comment Rules

## 1. Write comments for information the code cannot express clearly

A useful comment normally answers at least one of these:

- Why is this branch required?
- What problem does this workaround prevent?
- Why was this algorithm or parameter chosen?
- What invariant must remain true?
- What external condition does the code assume?
- Why must operations occur in this order?
- What unit, frame, sign convention, or state representation is being used?
- What unusual boundary condition is handled here?

Bad:

```cpp
// ret不等于0时返回
if (ret != 0)
    return ret;
```

Better:

```cpp
// 启动失败时直接透传底层错误码，调用方依赖该错误码区分状态错误和参数错误。
if (ret != 0)
    return ret;
```

## 2. Do not translate code into Chinese

Bad:

```cpp
// i加1
++i;

// 清空数组
memset(buf, 0, sizeof(buf));
```

Do not add a comment if the operation is already obvious.

## 3. Keep comments close to the decision they explain

Place a comment immediately before the smallest code region whose behavior it explains.

Do not place a large paragraph at the top of a function when the information applies only to one branch.

## 4. Prefer current reasoning over historical narrative

Version control records detailed edit history. Source comments should retain only history that still helps explain the current implementation.

Avoid:

```cpp
// 以前这里是A
// 后来改成B
// 然后又改成C
```

Prefer:

```cpp
// 使用C路径以避免设备切换期间读取到尚未稳定的状态。
```

## 5. Keep project terminology

Do not casually rename established domain concepts inside comments.

## 5.1 Modular comment prefix

For a nontrivial algorithm, behavior change, boundary condition, or engineering constraint, put the owning module before the detailed explanation using `模块：详细说明`. Typical module prefixes in the conveyor-tracking project include `去重：`、`排序：`、`传送带：`、`姿态：`、`涂胶：`、`通讯：`、`触发：` and `队列：`.

When a gyc change marker is present, the marker remains first and the module prefix follows it:

```cpp
// modified by gyc 2026-08-15：去重：统一使用归一化X和Y计算匹配分数
```

For a multi-line block:

```cpp
// modified by gyc 2026-08-15 start：去重：候选工件跨帧确认后才允许入队
...
// modified by gyc 2026-08-15 end
```

Choose one primary module for each comment. Do not rewrite unrelated historical comments solely to add a module prefix, and do not add prefixes to comments that only restate obvious syntax.

---

# gyc Change-Marking Convention

Use change markers only when modifying existing project code with a meaningful behavior change.

Supported categories:

- feature addition: `added by gyc`
- bug fix: `fixed by gyc`
- modification/optimization of existing behavior: `modified by gyc`

Date format:

```text
YYYY-MM-DD
```

Use the actual date on which the modification is made.

## 6. Single-line change: NEVER use start/end

If the actual code change is only one source-code line, add one explanatory marker immediately above that line.

Feature:

```cpp
// added by gyc 2026-08-12：增加断点复位状态记录
breakPoint.line = 1;
```

Bug fix:

```cpp
// fixed by gyc 2026-08-12：修正J5动力学零位偏移，避免重力项分解错误
q5_dyn = q5_ui + M_PI_2;
```

Modification:

```cpp
// modified by gyc 2026-08-12：调整速度滤波时间常数，降低短周期测量噪声
filter_time = new_filter_time;
```

Do not use `start/end` for a one-line source-code change.

## 7. Multi-line change: use start/end

If two or more source-code lines form one meaningful changed block, delimit the actual changed region.

Feature:

```cpp
// added by gyc 2026-08-12 start：增加过渡段采样过滤，避免瞬态数据进入辨识矩阵
if (sample_region == RBG_VALID)
{
    load_collect_point(...);
}
// added by gyc 2026-08-12 end
```

Bug fix:

```cpp
// fixed by gyc 2026-08-12 start：修复程序结束后断点未复位导致下次从旧行号启动的问题
strncpy(breakPoint.curProgName, mainProgName, BASIC_NAME_LENGTH);
breakPoint.line = 1;
// fixed by gyc 2026-08-12 end
```

Modification:

```cpp
// modified by gyc 2026-08-12 start：优化采样有效区判断，统一边界条件
const bool in_range = (q >= q_min && q <= q_max);
sample_valid = in_range && velocity_stable;
// modified by gyc 2026-08-12 end
```

## 8. The marker comes first; the start marker explains WHAT/WHY

Start:

```cpp
// added by gyc 2026-08-12 start：防止过渡段瞬态进入辨识矩阵
```

End:

```cpp
// added by gyc 2026-08-12 end
```

Do not repeat the full explanation in the end marker.

## 9. Mark only the lines actually changed

If adding one line inside another engineer's block, do not wrap the surrounding historical code.

```cpp
// 远程模式指定行启动 added by wyh 20241031 start
strncpy(...);
breakPoint.line = 1;

// added by gyc 2026-08-12：增加断点复位后的状态同步
sync_breakpoint_state();

rtapi_print_msg(...);
// added by wyh 20241031 end
```

Do not relabel the whole historical block as gyc.

## 10. Nested modification markers

A gyc block may appear inside another engineer's historical block if necessary, but keep the scope minimal and structurally valid.

Avoid deeply nested author blocks. If a change becomes large enough to make nesting confusing, refactor only if the task permits and behavior can be preserved safely.

## 11. Do not mark non-semantic edits

Normally do not add gyc markers for:

- formatting,
- indentation,
- whitespace,
- include ordering,
- spelling fixes,
- comment-only wording changes,
- automated formatting,
- behavior-neutral variable renaming,
- deleting clearly unused commented-out code,
- mechanical refactoring with no meaningful behavior change.

If such an edit is inseparable from a real feature/bug-fix block, the block may include it, but do not expand the marker range unnecessarily.

## 12. Choose the correct verb

Use `added by gyc` when new behavior or capability is introduced.

Use `fixed by gyc` when correcting incorrect behavior, crashes, wrong state, wrong math, wrong boundary handling, race conditions, or other defects.

Use `modified by gyc` when intentionally changing existing behavior, tuning a rule, reorganizing logic, or optimizing implementation without framing the old behavior as a defect.

Do not invent new verbs unless the project requires them.

## 13. Comment wording after the marker

Preferred pattern:

```cpp
// added by gyc YYYY-MM-DD：<功能目的、问题原因或工程约束>
```

or:

```cpp
// added by gyc YYYY-MM-DD start：<功能目的、问题原因或工程约束>
```

Good:

```cpp
// fixed by gyc 2026-08-12 start：执行完成后将断点复位到首行，避免远程再次启动时沿用旧断点
```

Weak:

```cpp
// fixed by gyc 2026-08-12 start：修改代码
```

Weak:

```cpp
// added by gyc 2026-08-12 start：增加判断
```

The change marker must come first. For a single-line marker, put the full-width colon and explanation after the date. For a multi-line start marker, put `start` before the full-width colon and explanation; the matching end marker stays short and contains no explanation. The description should allow a maintainer to understand the reason without opening Git history.

## 14. Preserve other engineers' markers

Do not rewrite another engineer's marker into a gyc marker. Do not alter the original author's date.

If the user's task explicitly removes or replaces the old feature, delete obsolete markers together with the obsolete code only when that deletion is part of the requested implementation.

## Review Checklist

Before finishing a code change:

- Does every nontrivial comment add information beyond the syntax?
- Are stale comments removed or updated?
- Is the change category correct: added / fixed / modified?
- Is the author exactly `gyc`?
- Is the date the actual current modification date?
- Is the date formatted `YYYY-MM-DD`?
- Is a one-line code change free of `start/end`?
- Does a multi-line block have matching start/end?
- Does the marker wrap only genuinely changed code?
- Are other engineers' markers preserved?
