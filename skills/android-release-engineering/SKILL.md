---
name: android-release-engineering
description: Android release engineering skill for signing, rollout strategy, release readiness, monitoring, and rollback planning. Use for production release planning and go/no-go decisions.
---

# Purpose

Guide reliable Android releases with operational readiness and risk control.

## When to use

- Preparing release candidate builds
- Defining staged rollout strategy
- Validating signing/distribution readiness
- Designing monitoring and rollback plans

## Workflow

1. Validate release readiness checklist.
2. Confirm signing and build integrity.
3. Define staged rollout and guardrails.
4. Prepare observability and incident responses.
5. Execute go/no-go recommendation.

## Output format

1. `Release readiness status`
2. `Blocking and non-blocking risks`
3. `Rollout plan`
4. `Monitoring plan`
5. `Rollback criteria`
6. `Post-release checks`

## Anti-pattern detection

- Big-bang rollout without guardrails
- Missing crash/performance monitoring gates
- Ambiguous rollback criteria
- Signing/configuration drift across environments
