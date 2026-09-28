# Algorithm and Mathematics Comment Rules

Comments around mathematical code should bridge the gap between equations and implementation.

## 1. Define symbols when mapping is not obvious

```cpp
// 重力模型：tau = m*g*l*sin(q)。
// q为J3相对重力方向的动力学角度，l单位m，tau单位N·m。
gravity_tau = mass * g * arm * sin(q);
```

## 2. Always make units explicit when mixed-unit mistakes are plausible

Examples: mm vs m, degree vs radian, N·mm vs N·m, kg·mm² vs kg·m², ms vs s, encoder counts vs joint angle.

Weak:

```cpp
x *= 0.001;
```

Better:

```cpp
// DH参数由mm转换为m后再进入动力学计算。
x *= 0.001;
```

## 3. State coordinate frame and sign conventions

```cpp
// rz定义在法兰坐标系中，+Z指向法兰外侧，因此外置负载的rz通常为正。
arm_z = l56 + rz;
```

## 4. Explain transformations, not every multiplication

For matrices or coordinate transforms, explain source frame, target frame, multiplication convention, and active/passive interpretation when relevant.

```cpp
// 右乘列向量：T_base_tool 将工具坐标中的点变换到基坐标系。
p_base = T_base_tool * p_tool;
```

## 5. Numerical methods

For filtering, fitting, optimization, integration, root finding, or differentiation, document method, important parameters, why it is used, assumptions, and boundary handling.

```cpp
// 使用11点三阶Savitzky-Golay局部多项式估计加速度，
// 在保留轨迹趋势的同时降低直接二阶差分对噪声的放大。
estimate_acceleration(...);
```

## 6. Approximation and heuristics

Mark approximations explicitly. Do not present an empirical approximation as an exact physical law.

## 7. Magic numbers

Replace with named constants when practical. If a literal must remain, explain its origin only when non-obvious.

```cpp
// 15%为当前界面用于提示拟合质量的工程阈值，不代表统计置信区间。
if (relative_error < 0.15)
```

## 8. Equation comments must match code

If code changes from `sin(q)` to `cos(q)`, update the formula comment in the same patch. Stale mathematical comments are more dangerous than missing comments.
