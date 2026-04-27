# Release Gates Reference

Use these as default starting gates, then adjust by app risk profile.

## Gate model

- Safety gates (must pass)
- Regression budget gates (relative to baseline)
- Observability gates (must be measurable)

Label each gate: `pass | at-risk | fail`.

## Default starting gates

1. Crash-free sessions:
   - `fail` if below team-defined absolute floor.
2. ANR rate:
   - `fail` if above team-defined absolute ceiling.
3. Startup/jank regression budget:
   - `fail` if regression exceeds agreed budget vs baseline.
4. Critical security issues:
   - `fail` when unresolved critical exploitability remains.

## Rollout strategy defaults

- Use staged rollout with explicit hold points.
- Stop/rollback when any safety gate flips to `fail`.
- For `at-risk` gates, reduce rollout speed and increase monitoring frequency.

## Evidence requirements

- Baseline and current metrics from comparable cohorts.
- Confidence in measurement quality documented.
- Known blind spots and compensating controls documented.
