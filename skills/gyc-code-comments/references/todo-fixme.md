# TODO / FIXME / NOTE / HACK / PERF Rules

Use markers consistently and only when they add actionable maintenance information.

## TODO

Use for planned, non-broken work.

```cpp
// TODO(gyc): 将固定滤波窗口改为参数配置；当前窗口长度与2ms采样周期绑定。
```

Avoid:

```cpp
// TODO: 优化
```

## FIXME

Use when current behavior is known to be wrong, incomplete, unsafe, or fragile.

```cpp
// FIXME(gyc): 断线重连后未重新同步驱动模式，可能导致首次指令被拒绝。
```

## HACK

Use only for a deliberate workaround that should not be mistaken for the ideal design.

```cpp
// HACK(gyc): 旧固件不会上报该状态位，暂以状态字组合推断；升级驱动后应移除。
```

## NOTE

Use for important contextual information that is not a task.

```cpp
// NOTE: 此处角度已经转换为动力学零位，后续禁止再次叠加90°偏置。
```

## PERF

Use for measured or structurally important performance constraints.

```cpp
// PERF: 控制周期内复用缓冲区，避免动态内存分配。
```

## REVIEW

Use when a decision needs human verification before being considered stable.

```cpp
// REVIEW(gyc): 该阈值来自现场经验值，量产前需要用新数据重新验证。
```

## Ownership and dates

For normal TODO/FIXME markers, `gyc` may be included as owner when useful.

Do not automatically append dates to every TODO/FIXME unless the project explicitly requires it.

The separate `added/fixed/modified by gyc YYYY-MM-DD` convention applies to actual code modifications, not to every maintenance note.

## Remove resolved markers

When a TODO/FIXME is fully resolved by the current change, remove the stale marker and add the appropriate change marker only if the actual implementation change qualifies under the project rule.

Do not leave a stale FIXME followed by a “fixed” comment after the defect has been resolved.
