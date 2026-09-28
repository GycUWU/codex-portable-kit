# C/C++ and Doxygen Rules

Use Doxygen for public interfaces and complex reusable APIs, not mechanically for every small `static` helper.

## 1. Public function documentation

Prefer:

```cpp
/**
 * @brief 启动一次负载辨识数据采集。
 *
 * 清空当前负载状态对应的采样批次并建立采集会话。
 * 本函数不执行最终参数拟合。
 *
 * @param motion      机器人运动控制对象。
 * @param load_state  空载或带载状态。
 * @return 0 表示成功；非0表示启动条件不满足。
 *
 * @note 调用前控制系统必须完成初始化。
 */
int cobot_id_start(Motion* motion, int load_state);
```

Document externally visible behavior, ownership/lifetime when non-obvious, units, valid ranges, state prerequisites, important side effects, and return/error semantics.

## 2. Do not restate types

Weak:

```cpp
/** @param count 数量 */
```

Better:

```cpp
/** @param count 本批次期望采样点数，必须小于等于 COBOT_LOAD_ID_MAX_SAMPLES。 */
```

## 3. Internal helpers

A small internal helper may need only a concise intent comment:

```cpp
// 仅在恒定激励区间采样，过渡段数据不进入回归矩阵。
static bool should_collect_sample(...);
```

Do not force full Doxygen on trivial private helpers.

## 4. Structs and fields

Document fields when meaning is not obvious from the type/name. Include units, coordinate frame, sign, ownership, state meaning, and valid range.

```cpp
typedef struct
{
    double rz;  ///< 负载质心沿法兰+Z方向的偏移，单位m，法兰外侧为正。
} LoadParam;
```

## 5. Enums and state machines

Describe state semantics, not just names.

```cpp
typedef enum
{
    LOAD_IDLE,       ///< 未采集，允许启动新会话。
    LOAD_RECORDING,  ///< 正在采样，不允许切换空载/带载状态。
    LOAD_READY       ///< 当前批次完整，可进入拟合。
} LoadState;
```

## 6. Header vs implementation

Put contract-level information in headers. Put implementation rationale, algorithm details, workarounds, and low-level constraints in source files near the implementation.

Avoid duplicating the same long explanation in both `.h` and `.c/.cpp`.

## 7. Callbacks

Document execution context/thread, ownership, whether blocking is allowed, callback lifetime, and whether reentrancy is possible when these are non-obvious.
