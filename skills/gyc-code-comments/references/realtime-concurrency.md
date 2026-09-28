# Realtime and Concurrency Comment Rules

Concurrency comments should explain ordering, ownership, visibility, and timing requirements.

## 1. Memory ordering

Weak:

```cpp
// 内存同步
__sync_synchronize();
```

Better:

```cpp
// 先保证采样数据全部写入，再发布save_flag。
// 否则读取线程可能先看到新标志但仍读到旧数据。
__sync_synchronize();
save_flag = 1;
```

## 2. Shared ownership

Document who writes and who reads shared state when non-obvious.

```cpp
// RT线程唯一写入；UI线程只读。更新通过generation计数发布完整快照。
```

## 3. Locks

Explain unusual lock boundaries.

```cpp
// 锁内只交换指针，数据处理放到锁外，避免阻塞2ms实时周期。
```

Do not narrate ordinary mutex syntax.

## 4. Lock-free structures

Document producer/consumer count, publication rule, wraparound behavior, overflow policy, and memory-order assumption when relevant.

## 5. Timing

State real timing requirements when they matter.

```cpp
// 该函数运行于2ms控制周期，不允许文件IO、动态内存分配或阻塞等待。
```

Do not invent a period from context if it is not established by code/config/user input.

## 6. Callbacks and threads

When a callback executes on a specific thread, say so if callers could otherwise misuse it.

```cpp
// EtherCAT周期线程回调：不得直接调用可能阻塞的UI或文件操作。
```

## 7. Atomics

Comment the invariant, not the atomic operation.

Weak:

```cpp
// 原子加1
counter.fetch_add(1);
```

Better:

```cpp
// generation为奇数表示写入中、偶数表示快照稳定。
counter.fetch_add(1);
```

## 8. Realtime performance comments

Use `PERF` only when there is a concrete performance constraint.

```cpp
// PERF: 该路径位于2ms周期内，避免重新分配vector容量。
```

## 9. Error handling across threads

Document whether an error is latched, edge-triggered, cleared by another thread, retryable, or affects data validity when those details are non-obvious.
