---
name: android-testing
description: Android testing strategy skill for unit, integration, UI, screenshot, contract, macrobenchmark, and baseline profile planning. Use this when users ask what to test, how much to test, or how to reduce flaky test suites.
---

# Purpose

Define realistic Android test strategies that maximize confidence while controlling cost and flakiness.

## When to use

- Creating or repairing test strategy for an app/module
- Balancing test pyramid scope and ROI
- Introducing Compose UI or screenshot tests
- Designing benchmark and baseline profile validation
- Improving flaky CI test pipelines

## Principles

1. Test behavior and contracts, not implementation trivia.
2. Keep most tests fast, isolated, and deterministic.
3. Escalate to integration/UI tests where risk justifies cost.
4. Make performance-critical flows measurable with benchmarks.
5. Treat flakiness as a production quality issue.

## Workflow

1. Map critical user and business flows.
2. Select test types per risk and boundary.
3. Define deterministic data/environment strategy.
4. Plan reliability controls for CI.
5. Add performance-oriented tests where justified.
6. Produce phased rollout plan.

## Output format

1. `Test pyramid recommendation`
2. `Test boundaries by layer`
3. `What not to test`
4. `Flakiness risks and controls`
5. `Performance test additions`
6. `Implementation sequence`

## Rules and restrictions

- Do not push broad UI tests when unit/integration can cover the same risk.
- Do not recommend testing private implementation details.
- Do not ignore flaky tests as "acceptable noise."
- Do not skip contract tests in integration-heavy boundaries.

## Anti-pattern detection

- UI-test-heavy suites with poor ROI
- Snapshot/screenshot tests with no review discipline
- Tests coupled to network/time randomness
- Missing failure-path tests on critical flows

## Related resources

- `templates/test-strategy.md`
