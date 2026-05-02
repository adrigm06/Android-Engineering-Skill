# Regression Pack Purpose

This pack exists to prevent quality drift after editing the Android master skill.

## Why it matters

- Ensures routing quality stays stable across domains.
- Detects policy regressions (constraints, authority precedence, confidence protocol).
- Makes refactors measurable instead of subjective.
- Enables before/after comparisons across skill versions.

## What is included

- `prompts.md`: 15 regression prompts covering architecture, compose, build, testing, performance, security, review, debugging, and release.
- `evaluation-rubric.md`: scoring model (0-16) and pass bands.
- `run_regression.py`: lightweight heuristic scorer for response files.
- `responses/`: place generated model responses as `Pxx.md`.

## How to run

1. Run prompts and save outputs into `responses/P01.md` to `responses/P15.md`.
2. Execute:

```bash
python assets/regression/run_regression.py --responses assets/regression/responses --output assets/regression/regression-report.json
```

3. Review JSON report and manually validate low-scoring prompts using the rubric.

## Notes

- The script is heuristic, not semantic truth.
- Final acceptance still requires rubric-based human review.
