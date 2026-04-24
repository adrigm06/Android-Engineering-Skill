---
name: android-performance
description: Android performance engineering skill focused on startup, jank, memory, ANRs, battery, tracing, and baseline profiles. Use whenever users ask to diagnose or optimize app performance.
---

# Purpose

Improve Android runtime performance using measurement-first diagnosis and targeted interventions.

## When to use

- Slow cold start or poor startup metrics
- UI jank and frame drops
- Memory pressure, GC churn, or ANR patterns
- Battery drain concerns
- Need for profiling/tracing and optimization roadmap

## Principles

1. Measure first, optimize second.
2. Prioritize top user-impact bottlenecks.
3. Use reproducible profiling scenarios.
4. Validate improvements with before/after metrics.
5. Avoid "micro-optimization theater."

## Workflow

1. Define performance goals and key journeys.
2. Collect baseline metrics and traces.
3. Identify highest-impact bottlenecks.
4. Propose targeted fixes with expected gains.
5. Validate with repeatable measurements.
6. Document guardrails to prevent regression.

## Output format

1. `Symptoms and probable bottlenecks`
2. `Profiling/instrumentation plan`
3. `Priority optimization plan`
4. `Expected impact and tradeoffs`
5. `Verification metrics`
6. `Regression prevention checklist`

## Rules and restrictions

- Do not optimize without instrumentation evidence.
- Do not overfit to synthetic benchmarks only.
- Do not recommend broad refactors when local fixes solve root causes.
- Do not ignore battery and thermal side effects.

## Anti-pattern detection

- Startup work overload on main thread
- Recomposition hot loops in Compose screens
- Memory leaks from lifecycle misuse
- Heavy background work with no battery budget

## Related resources

- `references/profiling-playbook.md`
