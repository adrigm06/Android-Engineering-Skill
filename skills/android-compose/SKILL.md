---
name: android-compose
description: Jetpack Compose engineering skill for state modeling, recomposition control, stability, and UI architecture. Use whenever the user asks to build, review, optimize, or debug Compose screens and navigation flows.
---

# Purpose

Design and review Compose UI with predictable state, stable composition, and testable screen architecture.

## When to use

- Building new Compose screens/components
- Reviewing recomposition or jank concerns
- Defining UI state and event models
- Designing Compose navigation patterns
- Improving previews and UI test strategy

## Principles

1. Keep UI state explicit and immutable.
2. Hoist state to the right owner.
3. Minimize unstable parameters across composable boundaries.
4. Keep side effects explicit and lifecycle-aware.
5. Keep composables focused and reusable by responsibility.

## Workflow

1. Define screen state model (`Loading`, `Content`, `Error`, etc.).
2. Split composable tree by responsibility.
3. Decide state ownership and hoisting boundaries.
4. Validate stability and recomposition hotspots.
5. Define event and navigation flows.
6. Propose preview and test coverage strategy.

## Output format

1. `UI state model`
2. `Composable structure`
3. `State hoisting strategy`
4. `Navigation/events model`
5. `Recomposition and stability risks`
6. `Preview/testing plan`
7. `Recommended fixes and next steps`

## Rules and restrictions

- Do not place business logic directly inside composables.
- Do not pass mutable state objects arbitrarily through deep trees.
- Do not hide side effects in rendering paths.
- Do not optimize blindly without profiling evidence.

## Anti-pattern detection

- Giant screen composables with mixed concerns
- Excessive `remember`/`derivedStateOf` misuse
- Unstable parameter graphs causing broad recompositions
- Navigation logic spread across unrelated composables

## Related resources

- `references/compose-state-patterns.md`
- `examples/common-pitfalls.md`
