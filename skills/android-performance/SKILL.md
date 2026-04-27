---
name: android-performance
description: Android performance engineering skill focused on startup, jank, memory, ANRs, battery, tracing, and baseline profiles. Use whenever users ask to diagnose or optimize app performance.
---

# Purpose

Improve Android runtime performance through evidence-driven diagnosis, targeted optimizations, and regression-resistant controls.

## Scope and authority

This skill is lead authority for runtime constraints:

- startup and first-frame latency
- frame-time stability and jank
- memory pressure and ANR behavior
- battery and thermal efficiency

Supporting interactions:

- align structural changes with `android-architecture`
- align Compose hot-path interventions with `android-compose`
- align release risk and rollback gates with `android-release-engineering`

## When to use

- slow startup, jank, ANR, memory, battery concerns
- optimization planning for critical user journeys
- performance regression investigation and prevention

## Decision engine workflow

1. Define user-impact goals and performance envelopes.
2. Capture baseline metrics and reproducible traces.
3. Rank bottlenecks by impact vs fix cost.
4. Choose intervention branch and expected gain.
5. Validate with before/after evidence.
6. Install guardrails against regression.

## Branching decision tree

### Branch A: bottleneck domain

- `startup-heavy`:
  - remove/defers main-thread initialization
  - prioritize first-frame and fully-drawn improvements
- `jank-heavy`:
  - isolate heavy UI/recomposition hotspots
  - reduce expensive work in frame-critical windows
- `memory/ANR-heavy`:
  - identify leak/allocation spikes and blocked thread patterns
- `battery-heavy`:
  - reduce unnecessary background work and polling

### Branch B: intervention aggressiveness

- `near release`:
  - prefer low-blast-radius fixes with measurable gain
- `post-release hardening window`:
  - allow deeper refactors if validated by benchmark/regression coverage

### Branch C: architecture tension

- if fastest fix violates boundaries:
  - choose constrained temporary workaround only with expiry criteria
  - define path back to target architecture

## Quantitative gates

Use measurable gates and label each `pass | at-risk | fail`:

- startup regression budget gate (relative to baseline)
- frame/jank regression budget gate (relative to baseline)
- memory/ANR safety gate (absolute + trend checks)
- battery/thermal regression gate (relative to baseline)

If no reliable baseline exists, return a measurement-first plan before committing deep optimizations.

## Tradeoff realism

Allow context-justified choices:

- a smaller guaranteed gain may beat risky large refactor near release
- defer low-impact tuning when top bottlenecks remain unresolved

Do not recommend optimization theater without measurable user impact.

## Uncertainty protocol

Always report confidence:

- `High` (>= 0.80)
- `Medium` (0.60-0.79)
- `Low` (< 0.60)

If confidence is medium/low:

- state instrumentation gaps and assumptions
- provide at least one conservative fallback
- request minimum additional traces/metrics to decide
- escalate to `android-architecture` or `android-compose` for cross-layer conflicts

## Cross-skill handoff payload

When escalating to/supporting other skills, include:

- `decision_domain`
- `requesting_skill: android-performance`
- `target_skill`
- `risk_class`
- `confidence` (band + numeric)
- `assumptions`
- `hard_constraints_checked`
- `quantitative_gates` (`pass | at-risk | fail`)
- `blocking_conflicts`
- `preferred_path`
- `fallback_path`
- `minimum_extra_evidence`

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

Also include:

- `Symptoms and probable bottlenecks`
- `Profiling/instrumentation plan`
- `Priority optimization plan`
- `Expected impact and tradeoffs`
- `Verification metrics`
- `Regression prevention controls`

## Anti-pattern detection

- optimize without baseline evidence
- broad refactor proposals for local bottlenecks
- ignoring battery/thermal regressions
- performance changes without guardrails or re-measurement

## Related resources

- `references/profiling-playbook.md`
