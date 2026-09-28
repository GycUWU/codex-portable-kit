# Algorithm Explanation

## Three-layer explanation

### Layer 1: intuition

Answer:

- What quantity are we trying to obtain?
- What physical/geometric relation makes it observable?
- What changes when inputs change?

Use a small concrete example when possible.

### Layer 2: mathematics

State:

- variables,
- coordinate frame,
- units,
- assumptions,
- equation,
- solution method.

Derive only the steps that explain the implementation. Do not add textbook derivation unrelated to the code.

### Layer 3: implementation

Map mathematical objects to code with a compact table when useful:

| Math | Code | Meaning | Unit |
|---|---|---|---|
| q | `joint_pos` | joint position | verify in source |
| τ | `torque` | joint torque | verify in source |

Only include mappings verified in source.

## Numerical methods

For filtering, fitting, integration, root finding, interpolation, optimization, or matrix solving, explain:

1. why this numerical method is used,
2. the actual input sequence/matrix,
3. parameter choices,
4. output,
5. numerical risks.

Possible risks include ill-conditioning, insufficient excitation, noise amplification by differentiation, singularity, parameter coupling, wrap-around, discontinuity, and unit mismatch.

Do not claim a parameter is optimal unless there is evidence.

## Robotics geometry

Always establish coordinate conventions before discussing signs.

For transforms/kinematics, distinguish base, joint/link, flange, tool/TCP, user/workobject, and sensor frames.

For angles, distinguish encoder zero, kinematic zero, mechanical zero, and UI-displayed zero.

For Cartesian orientation, identify the representation before manipulating it: Euler/RPY, axis-angle, quaternion, or rotation matrix.

## Trajectory topics

Distinguish:

- geometric path,
- path parameter,
- time parameterization,
- joint-space trajectory,
- Cartesian trajectory,
- interpolation,
- online trajectory generation.

Do not claim that synchronized joints imply a straight Cartesian TCP path without a kinematic argument.
