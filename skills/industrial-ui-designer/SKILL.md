---
name: industrial-ui-designer
description: Design, review, or refactor UI for industrial control, robotics, HMI, SCADA, machine configuration, realtime monitoring, diagnostics, motion control, process control, commissioning, engineering tools, and operational software where safety, state visibility, data density, stable layout, and fast operator decisions matter more than decorative branding.
---

# Industrial UI Designer

Design for operators and engineers who must understand system state quickly and act correctly.

Priority:
1. State visibility and operational safety.
2. Information hierarchy.
3. Stable interaction and predictable placement.
4. Dense but scannable data.
5. Error prevention and recovery.
6. Visual coherence.
7. Aesthetic refinement.

Do not design industrial software like a marketing site or consumer lifestyle app.

## Before design
Determine user role, primary operating scenario, normal/warning/fault states, realtime vs configuration workflow, target display size, input method, critical actions, alarm frequency, and data refresh characteristics.

## Route by page type
- Realtime operation: machine state, active mode, alarms, process values, motion/status feedback, immediate actions.
- Configuration: grouped parameters, units, validation, dependencies, defaults, safe apply/revert behavior.
- Diagnostics: timestamps, error codes, logs, IO/state inspection, cause/effect tracing, drill-down.
- Engineering visualization: curves, trajectories, coordinate systems, geometry, live numeric values, reproducible measurements.

## Layout
Prefer stable zones such as `navigation | workspace | contextual/diagnostic panel`.
Avoid card grids unless cards are genuinely independent objects. Use spacing, alignment, dividers, headers, and typography before containers.
Keep units adjacent to values. Distinguish target/configured values from feedback/actual values.

## Density
Industrial UI may be dense. Do not enlarge every control for “modernity.” Use hierarchy to separate primary state, operational values, secondary context, and metadata.

## Color
Color carries operational meaning. Maintain restrained semantic states: neutral, active, normal, warning, critical, disabled. Never use alarm colors decoratively. Do not rely on color alone.

## Typography
Use readable type, limited scales, and tabular numerals when useful. Avoid oversized headings and decorative fonts.

## Interaction
Critical actions require deliberate affordance: enable, reset, motion start, calibration overwrite, destructive changes. Confirm only when accidental activation has meaningful cost.

## Motion
Use animation only to explain state/spatial change. Do not add decorative entrance animation to operational screens. Realtime changes and alarms must remain immediate.

## Charts
Show units, axis meaning, series identity, current value/cursor when useful, and stable scales unless auto-scale is intentional. Avoid 3D chart effects.

## Tables
Treat tables as first-class components. Support fixed headers, sorting/filtering/resizing where useful. Keep row density appropriate for engineering use.

## Forms
Group by engineering meaning. Show units, ranges, validation, read-only state, dependency/enable conditions, and safe apply/revert behavior.

## Avoid
- giant hero text
- gradient blobs
- excessive glassmorphism
- rounded-card-everywhere layouts
- decorative charts
- oversized empty space
- neon cyberpunk without product justification
- hiding critical state behind tabs

## Review
Load `references/industrial-review.md` before finalizing. When redesigning existing UI, explain the operational problem first, then the visual change. For rendered UI, inspect target-size screenshots and iterate.
