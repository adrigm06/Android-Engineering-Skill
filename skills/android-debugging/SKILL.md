---
name: android-debugging
description: Android debugging skill for root-cause analysis using hypothesis-driven workflows, reproduction plans, instrumentation, and narrowing strategies. Use when bugs are intermittent, hard to reproduce, or cross-layer.
---

# Purpose

Diagnose Android issues with a repeatable, evidence-driven debugging process.

## When to use

- Intermittent crashes or inconsistent behavior
- Environment-specific failures
- Cross-layer bugs (UI/domain/data/build/runtime)
- Regression introduced by recent changes

## Workflow

1. Define symptom precisely.
2. Build reproducible scenario matrix.
3. Generate ranked hypotheses.
4. Add instrumentation/logging/tracing.
5. Narrow via controlled experiments.
6. Propose fix candidates and validation plan.

## Output format

1. `Observed symptoms`
2. `Most likely root causes`
3. `Reproduction strategy`
4. `Instrumentation plan`
5. `Narrowing experiments`
6. `Fix candidates and verification`

## Anti-pattern detection

- Guess-based fixes without evidence
- No reproducible scenario baseline
- Logging noise without diagnostic intent
- Premature refactor before root cause
