# Debugging Playbook

## Hypothesis-driven loop

1. Define failure envelope precisely.
2. Rank hypotheses by likelihood and blast radius.
3. Instrument only what discriminates top hypotheses.
4. Run controlled experiments.
5. Update ranking and confidence.

## Reproducibility matrix

Track by:

- device/os/app version
- network/account state
- feature flags/config
- foreground/background lifecycle state

## Confidence guidance

- `High` (>= 0.80): reproducible root cause + converging evidence
- `Medium` (0.60-0.79): plausible root cause, partial evidence
- `Low` (< 0.60): weak or conflicting signals

When medium/low, request minimum additional evidence before deep refactors.

## Escalation triggers

- escalate to `android-performance` when symptoms indicate startup/jank/memory/ANR bottlenecks
- escalate to `android-security` when issue may expose data or bypass controls
- escalate to `android-release-engineering` when production impact requires containment/rollback
