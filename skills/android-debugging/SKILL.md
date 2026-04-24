---
name: android-debugging
description: Android debugging skill for root-cause analysis using hypothesis-driven workflows, reproduction plans, instrumentation, and narrowing strategies. Use when bugs are intermittent, hard to reproduce, or cross-layer.
---

# Purpose

Diagnose Android issues with hypothesis-ranked investigation, reproducible experiments, and evidence-based root-cause closure.

## Scope and authority

This skill is root-cause authority for incident triage and narrowing workflow.

## When to use

- intermittent crashes and inconsistent behavior
- cross-layer regressions
- environment- or device-specific failures

## Decision engine workflow

1. Define symptom, scope, and impact.
2. Build reproducibility matrix.
3. Rank hypotheses by likelihood and blast radius.
4. Add targeted instrumentation.
5. Run narrowing experiments and update confidence per hypothesis.
6. Propose fix candidates and verification path.

## Branching decision tree

### Branch A: reproducibility state

- `reproducible`:
  - run controlled experiments and binary-search recent changes
- `non-reproducible`:
  - invest first in telemetry and environment narrowing before proposing fixes

### Branch B: incident severity

- `production-impacting`:
  - optimize for fast containment and rollback-safe mitigation
- `non-blocking`:
  - optimize for high-confidence root-cause isolation before code change

## Uncertainty protocol

Always provide confidence per primary hypothesis.
If confidence remains low, widen instrumentation and escalate to supporting skill by domain.

## Output contract

Follow global order from `AGENTS.md`:

1. `Context and constraints`
2. `Decision and rationale`
3. `Alternatives considered`
4. `Tradeoffs`
5. `Risks and mitigations`
6. `Confidence and unknowns`
7. `Cross-skill impacts`
8. `Next implementation steps`

Then include debugging-specific artifacts:

- `Observed symptoms`
- `Most likely root causes`
- `Reproduction strategy`
- `Instrumentation plan`
- `Narrowing experiments`
- `Fix candidates and verification`

## Anti-pattern detection

- guess-based fixes without evidence
- no reproducible baseline
- noisy logs without diagnostic hypothesis
- deep refactor before root cause confirmation
