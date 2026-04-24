---
name: android-gradle-build
description: Android build engineering skill for Gradle architecture, convention plugins, dependency management, and build performance. Use whenever users ask to optimize build time, modular build setup, or dependency strategy.
---

# Purpose

Improve build reliability and speed through maintainable Gradle structure and dependency discipline.

## When to use

- Build time optimization efforts
- Multi-module Gradle setup design
- Convention plugin/build-logic migration
- KSP vs kapt strategy decisions
- CI cache and reproducibility improvements

## Principles

1. Keep build logic centralized and reusable.
2. Use version catalogs as the dependency source of truth.
3. Prefer incremental, measurable build optimizations.
4. Avoid dynamic/implicit Gradle behavior that hurts reproducibility.
5. Split modules only when it improves ownership or build isolation.

## Workflow

1. Capture baseline metrics (configuration time, clean/incremental builds).
2. Audit dependency graph and plugin duplication.
3. Propose build-logic and convention plugin structure.
4. Choose annotation processing strategy (KSP/kapt) per module constraints.
5. Apply caching and CI-safe optimizations.
6. Define migration sequence with rollback points.

## Output format

1. `Current build pain points`
2. `Proposed build layout`
3. `Dependency/version strategy`
4. `Performance interventions`
5. `CI/cache strategy`
6. `Migration plan`
7. `Risk controls`

## Rules and restrictions

- Do not recommend premature module explosion.
- Do not optimize without baseline and post-change metrics.
- Do not use `api` dependencies unless transitive exposure is intentional.
- Do not treat cache misses as acceptable without root cause analysis.

## Anti-pattern detection

- Repeated Gradle snippets across modules with no convention plugin
- Overuse of `api` leading to classpath bloat
- Unpinned dependency/plugin versions
- Annotation processor misuse in hot build paths

## Related resources

- `references/build-optimization-checklist.md`
