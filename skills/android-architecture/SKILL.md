---
name: android-architecture
description: Architecture strategy for Android apps at real production scale. Use this whenever the user asks about app structure, modularization, MVVM/MVI/UDF choices, migration from legacy code, dependency boundaries, or architecture review decisions.
---

# Purpose

Design and review Android architecture with explicit tradeoffs, enforceable module boundaries, and practical migration paths.

## When to use

Use this skill when the user is:

- Starting a new Android app architecture
- Refactoring package/module structure
- Migrating legacy code toward cleaner boundaries
- Deciding between MVVM, MVI, UDF, or Clean Architecture depth
- Asking for dependency rules or module decomposition
- Requesting ADR-ready architecture decisions

## Inputs to gather

- Team size and ownership model
- Product complexity (features, domains, release cadence)
- Current architecture state and pain points
- Build time and CI constraints
- Regulatory/security requirements
- Migration risk tolerance and timeline

## Skill-specific principles

1. Optimize for maintainable boundaries, not maximal layering.
2. Keep domain pure and framework-independent.
3. Use module boundaries to represent ownership and change rate.
4. Separate API contracts from implementation details.
5. Prefer evolutionary migration over big-bang rewrites.
6. Trade architecture complexity only when it pays back.

## Workflow

1. Interpret context and constraints.
2. Select architecture style and state model fit.
3. Propose package/module topology.
4. Define dependency direction and visibility rules.
5. Evaluate tradeoffs, risks, and migration effort.
6. Produce implementation-ready output + ADR draft.

## Decision heuristics

### Architecture depth

- Small team + low domain complexity -> modular monolith + package-by-feature.
- Growing team + medium complexity -> selective multi-module by ownership.
- Multi-team + high complexity -> feature modules + strong core/domain contracts.

### State management style

- Mostly form/list flows -> MVVM with clear UI state.
- Event-heavy, complex state transitions -> MVI/UDF.
- Cross-feature business rules and policies -> deeper Clean Architecture boundaries.

## Output format

Always return this structure:

1. `Context`
2. `Recommended architecture style`
3. `Proposed module tree`
4. `Dependency rules (allowed/forbidden)`
5. `Tradeoffs and alternatives`
6. `Risks and mitigations`
7. `Migration path (if legacy)`
8. `ADR draft`
9. `First 3 implementation steps`

## Rules and restrictions

- Do not recommend feature-to-feature dependencies.
- Do not place data-source details inside domain interfaces.
- Do not over-split modules without ownership/build rationale.
- Do not prescribe patterns without a context fit explanation.

## Anti-pattern detection

Flag and explain:

- God modules with mixed concerns
- Fake Clean Architecture with pass-through layers
- Use-case explosion with little domain value
- Repositories leaking transport/storage details to UI
- Premature multi-module fragmentation

## Related resources

- `references/architecture-selection.md`
- `references/module-boundaries.md`
- `templates/architecture-proposal.md`
- `templates/adr.md`
- `examples/anti-patterns.md`
