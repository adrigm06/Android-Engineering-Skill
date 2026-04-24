# Android Engineering Skill Package - Context

## Purpose

This document defines the design contract for building and evolving a professional Android skill system.

The repository focuses on Android engineering workflows:
architecture, Compose, build systems, testing, performance, security, debugging, code review, and release engineering.

## Core model

```text
Global Context (AGENTS.md)
    -> Domain Skills (skills/*/SKILL.md)
        -> References + Templates + Examples
```

- `AGENTS.md` carries cross-cutting rules.
- Skills provide specialized reasoning and outputs.
- References/templates/examples keep skills maintainable and reusable.

## Quality bar

This package should emulate a senior engineering profile:

- Android Staff Engineer
- Build Engineer
- Performance and Security reviewer

Guidance must be:

- Structured and actionable
- Explicit about tradeoffs
- Context-aware (team size, app maturity, constraints)
- Maintainable for open-source contributors

## Design principles

1. Keep skills small and focused.
2. Avoid duplicating global rules inside each skill.
3. Prefer decision criteria over checklists.
4. Detect anti-patterns, not only "best practices."
5. Make migration paths explicit for legacy codebases.
6. Favor practical recommendations over purity.
7. Keep repository growth manageable through clear conventions.

## Scope boundaries

In scope:

- Android architecture and modularization
- Jetpack Compose engineering
- Gradle and build performance
- Testing strategy and reliability
- Runtime performance engineering
- Mobile security controls

Out of scope:

- Backend architecture deep dives
- Non-Android UI frameworks unless needed for integration context
- Generic software advice without Android implications

## Evolution strategy

- Add skills only when a domain has clear boundaries and reusable patterns.
- Keep `SKILL.md` concise; move depth to `references/`.
- Add templates when output format repeats across tasks.
- Add examples when teams frequently misapply patterns.

This file is the design anchor for future iterations.
