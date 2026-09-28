# Robotics and Control Comment Rules

Robotics comments should remove ambiguity around frames, motion semantics, states, and hardware meaning.

## 1. Coordinate frames

When relevant, identify base/world, user, tool/TCP, flange, workpiece, camera, or conveyor dynamic frame.

```cpp
// target_pose位于动态传送带用户坐标系中，执行前转换到机器人基坐标系。
```

## 2. Axis and angle conventions

Document joint index, zero position, positive direction, degree/radian, and controller zero vs dynamics zero.

```cpp
// q5_ui为示教器显示角度；动力学模型零位相对其偏置+90°。
q5_dyn = q5_ui + M_PI_2;
```

## 3. Path vs trajectory

Use terminology precisely:

- path: geometric locus,
- trajectory: geometry plus time law,
- interpolation: generating intermediate samples,
- OTG: online trajectory generation.

Do not call every motion-planning operation “路径规划”.

## 4. Position / velocity / acceleration / jerk

When buffers or arrays store these values, document units and whether they are commanded, planned, filtered, or measured.

```cpp
// update_vel为本周期滤波后的传送带速度，单位mm/s；不是编码器原始差分值。
```

## 5. Payload identification

Clarify empty/load batch, main/auxiliary joint, measured or current-estimated torque, sample-valid region, filtering, regression target, coordinate frame for COM, and inertia units.

Avoid comments that imply a sensor exists when torque is actually estimated from motor current.

## 6. EtherCAT / drive / IO

For PDO or object-dictionary code, prefer comments that name the semantic object.

```cpp
// CiA402 0x6041 Statusword：读取驱动当前状态机状态。
```

Do not overload comments with protocol tutorials. For RxPDO/TxPDO, follow the project's master/slave perspective consistently.

## 7. State machines

Explain transitions when the trigger is non-obvious.

```cpp
// 只有本批次采样完整且未发生overflow时才允许进入READY，
// 防止不完整数据被错误并入历史辨识统计。
```

## 8. Motion safety and critical actions

Explain safety-related conditions without overstating certification or guarantees.

```cpp
// 未完成伺服状态确认前禁止下发运动指令，避免状态切换期间指令被驱动拒绝。
```

Avoid vague claims such as “保证绝对安全”.

## 9. Calibration

State what is calibrated, reference frame, reference point, prerequisite, persisted result, and invalidation conditions when these are non-obvious.

## 10. Realtime loops

Do not add long prose inside hot loops. Put concise comments at relevant decision points or function boundaries.
