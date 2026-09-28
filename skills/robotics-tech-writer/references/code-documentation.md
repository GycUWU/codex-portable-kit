# Code Documentation

## Explain relationships before details

Start with the module's role and main path.

Bad order:

- function A
- function B
- struct C
- macro D

Better order:

- what enters the subsystem,
- where state lives,
- how calls move through the subsystem,
- which functions implement each stage.

## Structures

For an important structure, explain:

- responsibility,
- lifetime,
- who initializes it,
- who mutates it,
- which fields matter for this feature,
- invariants,
- concurrency or visibility constraints when relevant.

Do not turn every field into a dictionary if most fields are irrelevant.

## Functions

For an important function, cover only useful dimensions:

- purpose,
- inputs/outputs,
- preconditions,
- key steps,
- state changes,
- error/return paths,
- caller/callee relationship.

Avoid paraphrasing obvious syntax.

## Call chains

Represent a call chain compactly, for example:

`external command -> session start -> data collection -> fit -> validation -> result publication`

Then explain each transition.

## Macros/constants

Explain a constant when it affects physical scale, array capacity, sample count, thresholds, state machine, protocol mapping, numerical stability, or timing.

Do not list constants with no narrative role.

## Concurrency and realtime

When applicable, explicitly document:

- task/thread context,
- sampling period,
- lock/atomic/barrier behavior,
- real-time restrictions,
- producer/consumer relationship,
- visibility guarantees.

Only claim timing determinism when the source supports it.

## Configuration

For configuration-driven behavior, connect:

`configuration key -> parsed field -> runtime consumer -> effect`

This is more useful than describing the configuration file in isolation.
