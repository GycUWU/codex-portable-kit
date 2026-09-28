# Bug Analysis and Fix Record

A useful bug document should answer why the bug existed, not just list changed lines.

## Evidence chain

Build:

`symptom -> reproduction -> observed data -> failing code path -> root cause -> fix -> verification`

## Root cause standard

A root cause should be specific enough that a maintainer can explain why the old code produced the symptom.

Weak:

> The algorithm had a problem.

Strong only when supported:

> The implementation used one angle-zero convention while the dynamics term assumed another, introducing a systematic phase shift in the gravity decomposition.

## Fix explanation

Describe:

- what changed,
- why that change addresses the root cause,
- what behavior intentionally remains unchanged,
- what new assumptions were introduced.

## Verification

Prefer regression tests, before/after logs, numeric comparison, trajectory plots, known physical cases, or boundary tests.

Do not treat “compiled successfully” as sufficient verification for a behavioral bug.

## Risk

State remaining risk when relevant:

- untested branch,
- limited sample range,
- hardware dependence,
- calibration dependence,
- legacy compatibility,
- numerical edge case.
