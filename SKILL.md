---
name: android-engineering-skill
description: Unified Android master skill that routes, composes, and synthesizes architecture, compose, gradle build, testing, performance, security, code review, debugging, and release engineering decisions for Kotlin Android projects.
---

# Android Engineering Master Skill

Use this as the single Android entrypoint. It orchestrates the domain skills in `skills/` and returns one integrated decision.

Global policy, non-negotiables, authority model, quantitative gates, and output contracts are defined in `AGENTS.md`.

## Primary objective

- Provide one complete Android skill for end-to-end engineering work.
- Keep modular depth by delegating domain-heavy reasoning to `skills/*/SKILL.md`.
- Avoid conflicting advice by using the authority protocol from `AGENTS.md`.

## Operating workflow (mandatory)

1. Assess project context and constraints using `assets/project-context-assessment.md`.
2. Classify mode: Design, Review, Generation, or Debug.
3. Select lead domain skill and supporting skills with `assets/routing-matrix.md`.
4. Execute lead-skill decision flow; pull only required supporting constraints.
5. Resolve conflicts with authority protocol and quantitative gates from `AGENTS.md`.
6. Run Validation stage: Plan -> Validate -> Execute.
7. Return one integrated output using the global output contract.

## Validation stage (mandatory before final output)

- **Plan**: define proposed path, risk class, expected impact, and verification gates.
- **Validate**: confirm minimum required evidence exists; if not, downgrade confidence and define minimum extra evidence.
- **Execute**: deliver final recommendation with explicit `pass | at-risk | fail` gate status and rollback-safe next steps.

If required evidence is missing, do not present a false-final answer. Return a measurement-first plan.

## Routing matrix (quick map)

- Architecture, modularization, dependency direction -> `skills/android-architecture/SKILL.md` (lead)
- Compose UI state/recomposition/navigation -> `skills/android-compose/SKILL.md` (lead)
- Build times, Gradle architecture, dependency governance -> `skills/android-gradle-build/SKILL.md` (lead)
- Test strategy, flaky suites, confidence depth -> `skills/android-testing/SKILL.md` (lead)
- Startup/jank/memory/ANR/battery optimization -> `skills/android-performance/SKILL.md` (lead)
- Secrets, trust boundaries, sensitive data controls -> `skills/android-security/SKILL.md` (lead, critical override)
- PR/technical debt quality synthesis -> `skills/android-code-review/SKILL.md` (lead)
- Root-cause investigation and narrowing -> `skills/android-debugging/SKILL.md` (lead)
- Go/no-go, rollout, rollback, release guardrails -> `skills/android-release-engineering/SKILL.md` (lead)

For multi-domain tasks, set exactly one lead skill and add only materially relevant supporting skills.

## Project context adaptation

### Greenfield
- Start with modular monolith unless ownership/build pain justifies deeper split.
- Prefer Kotlin + Compose + coroutines + Room + Hilt + KSP + version catalogs.
- Establish CI, test strategy, and release gates from day one.

### Legacy modernization
- Prioritize pain-first increments; avoid big-bang rewrites.
- Stabilize boundaries before style purity.
- Use rollback-safe migration slices with explicit temporary compromises.

### Enterprise / multi-team
- Enforce strict ownership boundaries and module contracts.
- Increase release and security rigor; require stronger evidence gates.
- Optimize for long-term maintainability and team scalability.

### Startup / MVP
- Optimize for delivery speed with explicit debt labeling.
- Protect critical flows with focused testing and release guardrails.
- Keep upgrade paths documented for every pragmatic shortcut.

## Mode contract shortcuts

- Design -> recommend architecture/implementation direction + alternatives + decision triggers.
- Review -> findings by severity with evidence, risk, fix, and verification.
- Generation -> implementation plan/code strategy aligned to constraints and rollback-safe sequencing.
- Debug -> ranked hypotheses, reproduction plan, instrumentation, and confidence updates.

## Required behavior

- Do not bypass non-negotiable constraints.
- Do not produce independent checklists per domain; synthesize one plan.
- Do not present temporary compromises as permanent architecture.
- Always include confidence and assumptions for non-trivial recommendations.

## Mandatory output block (non-trivial responses)

Include this compact block in all non-trivial outputs:

- `Lead domain`: selected lead skill.
- `Supporting domains`: only materially relevant supporting skills.
- `Top gates`: 2-4 key gates labeled `pass | at-risk | fail`.
- `Minimum extra evidence`: smallest missing inputs that could change the decision.

## Key assets

- Global runtime policy: `AGENTS.md`
- Project context worksheet: `assets/project-context-assessment.md`
- Routing matrix: `assets/routing-matrix.md`
- Domain catalog: `skills/README.md`
