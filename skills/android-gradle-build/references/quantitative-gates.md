# Build Quantitative Gates

Use these as default starter gates and tune per repository baseline.

## Gate labels

- `pass`
- `at-risk`
- `fail`

## Core build gates

- Configuration time regression budget (vs baseline)
- Clean build regression budget (vs baseline)
- Incremental build regression budget (vs baseline)
- Cache effectiveness trend (hit-rate and determinism)

## Decision policy

- If any safety-critical build gate is `fail`, pause risky build-graph changes.
- If multiple gates are `at-risk`, prioritize measurement and deterministic inputs before further optimization.
- If baselines are missing, run measurement-first and avoid irreversible changes.
