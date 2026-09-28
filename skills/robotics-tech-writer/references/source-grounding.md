# Source Grounding

## Goal

Make every technical claim traceable to evidence.

## Evidence classes

Classify important claims mentally as one of:

- `SOURCE`: directly supported by code, configuration, test, log, spec, or user-provided source.
- `OBSERVED`: demonstrated by runtime output, test result, measurement, or log.
- `INFERENCE`: reasonable conclusion from multiple source facts, but not explicitly stated.
- `UNKNOWN`: not established by available material.

Do not label every sentence in the final document. Use labels only where uncertainty matters.

## Code reading sequence

For a nontrivial feature:

1. Find the entry point or external call.
2. Find declarations and relevant structures.
3. Trace the call chain.
4. Find state mutations.
5. Find configuration reads.
6. Find output, errors, and completion conditions.
7. Search call sites for assumptions.
8. Check tests/logs for demonstrated behavior.
9. Check comments last when they conflict with behavior.

## Do not infer from names alone

A function named `calibrate()` does not prove what it calibrates.
A variable named `velocity` does not establish its unit.
A comment saying “position” does not establish coordinate frame.

Verify through definitions, consumers, conversions, constants, or surrounding protocol.

## Formula grounding

For each important formula, locate:

- input source,
- unit conversion,
- sign convention,
- coordinate frame,
- constant origin,
- output consumer.

If a formula in documentation differs from the current implementation, present the discrepancy explicitly.

## Branch and version awareness

When multiple branches or implementations exist:

- identify which one is being documented,
- do not merge behaviors across branches unless asked,
- call out code paths that are legacy, dead, conditional, or platform-specific.

## External knowledge

Use outside documentation only when requested or needed to explain a standard.

Keep a boundary between:

- what the project does,
- what the standard says,
- what you infer.

Do not rewrite project behavior to match how a standard “should” work.
