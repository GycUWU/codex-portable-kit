# Robotics and Control Terminology

Use project terminology first. These conventions are defaults only.

## Motion

Distinguish:

- 路径（path）: geometric locus, independent of timing.
- 轨迹（trajectory）: path plus time law / state over time.
- 插补（interpolation）: generate intermediate references between points.
- 轨迹规划（trajectory planning）: construct feasible time-parameterized motion.
- 在线轨迹生成（OTG）: update a feasible trajectory online from current/target states.

## State derivatives

Use position/位置, velocity/速度, acceleration/加速度, and jerk/加加速度 consistently with the project.

Do not call jerk “加速度” or “冲击” without context.

## Frames

Identify actual project names for base/world, flange, tool/TCP, user/workobject, sensor/camera, and conveyor/dynamic user frames.

Do not silently assume axes or handedness.

## EtherCAT / CiA 402

When present, distinguish:

- RxPDO: master-to-slave process data.
- TxPDO: slave-to-master process data.
- Controlword vs Statusword.
- target position vs position actual value.
- EtherCAT AL state vs CiA 402 drive state.

Verify object indexes in the target configuration before documenting them.

## Identification / fitting

Distinguish raw measurement, filtered signal, regressor/design matrix, fitted parameter, residual, RMS error, relative error, and physical validation.

Do not call residual RMS an “accuracy percentage” unless a normalization is defined.
