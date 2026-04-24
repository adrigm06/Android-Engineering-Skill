# Skills Catalog

This directory contains domain skills that compose into a unified Android decision system.

## Core decision domains

- `android-architecture`: structural authority for boundaries, layering, and modularization
- `android-compose`: UI runtime authority for Compose state/recomposition/navigation decisions
- `android-gradle-build`: build graph and CI authority for Gradle architecture and performance
- `android-testing`: quality confidence authority for verification depth and flakiness strategy
- `android-performance`: runtime authority for startup/jank/memory/ANR/battery decisions
- `android-security`: global critical override for exploitability and sensitive data controls

## Operational domains

- `android-code-review`: severity-based synthesis across domains
- `android-debugging`: hypothesis-driven root-cause workflow
- `android-release-engineering`: production gate authority for rollout and go/no-go

## Composition rules

- Use one lead skill for the dominant decision domain.
- Add supporting skills only for material constraints.
- Resolve conflicts using authority protocol in `AGENTS.md`.
- Return one integrated decision, not independent checklists.
