# Android Engineering Skill Package

A modular, composable, production-grade Android skill system for agentic engineering workflows.

This package is designed to behave like a senior Android Staff Engineer under real constraints, not like a generic checklist assistant.

## What this is

This repository is an open-source decision engine for Android engineering tasks:

- architecture and modularization
- Compose UI system design
- Gradle/build and CI strategy
- testing strategy and quality confidence
- performance, security, debugging, and release readiness

The system is built for multi-skill composition and deterministic conflict resolution.

## Mental model

Think of the package as three layers:

1. `AGENTS.md` defines runtime constraints and arbitration protocol.
2. `skills/*/SKILL.md` defines domain execution logic and decision branches.
3. `references/`, `templates/`, and `examples/` provide depth and reusable artifacts.

This layering keeps policy stable, skills focused, and contributions maintainable.

## Why this exists

Most assistant configurations collapse into one giant prompt that drifts over time.
This package uses explicit modularity and authority boundaries to avoid that failure mode.

Core goals:

- internal coherence across skills
- deterministic decisions under conflict
- tradeoff-aware recommendations with risk visibility
- production realism over theoretical purity
- open-source contributor scalability

## Decision engine behavior

The system upgrades from "skill checklist" to "skill decision engine":

- each skill branches by context, constraints, and risk
- uncertainty is explicit via confidence levels and assumptions
- cross-skill conflicts resolve through authority model, not prompt ordering
- outputs follow one global contract across all domains

## Cross-skill authority highlights

- `android-security`: global critical override for exploitability and sensitive data risk
- `android-architecture`: structural authority for boundaries and layering
- `android-release-engineering`: production gate authority for go/no-go and rollback policy
- `android-performance`: runtime authority for startup/jank/memory/ANR/battery constraints
- `android-gradle-build`: build graph and CI authority
- other skills provide domain execution and synthesis

Full protocol is defined in `AGENTS.md`.

## Included skills

- `android-architecture`
- `android-compose`
- `android-gradle-build`
- `android-testing`
- `android-performance`
- `android-security`
- `android-code-review`
- `android-debugging`
- `android-release-engineering`

## Repository layout

```text
AGENTS.md                  # Runtime rules, authority, conflict protocol
CONTEXT.md                 # Product philosophy and system design intent
skills/<skill-name>/
  SKILL.md                 # Triggering + decision logic + output contract usage
  references/              # Deep guidance and decision support
  templates/               # Reusable response artifacts
  examples/                # Good/bad pattern contrasts
```

## Output quality baseline

All non-trivial outputs follow the same section order:

1. Context and constraints
2. Decision and rationale
3. Alternatives considered
4. Tradeoffs
5. Risks and mitigations
6. Confidence and unknowns
7. Cross-skill impacts
8. Next implementation steps

## Open-source readiness

The repository includes:

- contribution and review policy in `CONTRIBUTING.md`
- security disclosure process in `SECURITY.md`
- semantic changelog in `CHANGELOG.md`
- issue templates in `.github/ISSUE_TEMPLATE/`

## Evolution policy

- evolve by improving decision quality and conflict determinism
- preserve stable skill names and trigger intent unless strongly justified
- document material behavior changes in `CHANGELOG.md`

## Contributing

See `CONTRIBUTING.md` for contribution standards, compatibility expectations, and review requirements.

## License

MIT License. See `LICENSE`.
