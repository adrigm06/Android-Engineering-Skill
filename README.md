# Android Engineering Skill Package

![Platform: Android](https://img.shields.io/badge/Platform-Android-3DDC84?logo=android&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

A modular, production-oriented Android skill package for agentic engineering workflows.

## Purpose

This repository is an open-source decision engine for high-impact Android engineering work:

- Architecture and modularization
- Compose UI state and design systems
- Gradle/build and CI strategy
- Testing strategy and confidence planning
- Performance, security, debugging, and release readiness

The package is built for multi-skill composition and deterministic conflict resolution.

## Install with npx

Install a local copy with:

```bash
npx @adrigm06/android-engineering-skill
```

By default this creates `./android-engineering-skill` in the current directory.

Optional target directory:

```bash
npx @adrigm06/android-engineering-skill ./path/to/install
```

## Mental Model

The system uses four layers to keep policy stable and domain logic focused:

1. `SKILL.md`: master entrypoint and routing
2. `AGENTS.md`: runtime constraints and conflict arbitration
3. `skills/*/SKILL.md`: domain logic and decision branching
4. `assets/`, `references/`, `templates/`, `examples/`: reusable support artifacts

## Cross-Skill Authority

Domain conflicts are resolved through an explicit authority model defined in `AGENTS.md`.

| Domain | Authority | Primary responsibility |
| :--- | :--- | :--- |
| `android-security` | Critical / global override | Exploitability and sensitive data risk |
| `android-architecture` | Structural | Module boundaries and dependency direction |
| `android-release-engineering` | Production gate | Go/no-go, rollout, and rollback policy |
| `android-performance` | Runtime | Startup, jank, memory, ANR, battery |
| `android-gradle-build` | Build/CI | Build graph and CI constraints |

## Included Skills

- `android-architecture`
- `android-compose`
- `android-gradle-build`
- `android-testing`
- `android-performance`
- `android-security`
- `android-code-review`
- `android-debugging`
- `android-release-engineering`

## Repository Structure

```text
.
|- SKILL.md                   # Master entrypoint and routing
|- AGENTS.md                  # Runtime rules and conflict protocol
|- CONTEXT.md                 # Product philosophy and intent
|- assets/                    # Routing and evaluation assets
`- skills/
   `- <skill-name>/
      |- SKILL.md             # Domain decision logic and output contract usage
      |- references/          # Deep guidance
      |- templates/           # Reusable response artifacts
      `- examples/            # Good vs bad pattern contrasts
```

## Output Quality Baseline

All non-trivial outputs follow the same section order:

1. Context and constraints
2. Decision and rationale
3. Alternatives considered
4. Tradeoffs
5. Risks and mitigations
6. Confidence and unknowns
7. Cross-skill impacts
8. Next implementation steps

## Contributing and Evolution

- Improve decision quality and conflict determinism
- Keep skill names and trigger intent stable unless strongly justified
- Document material behavior changes in `CHANGELOG.md`

See `CONTRIBUTING.md` for contribution standards and compatibility expectations.

## License

MIT. See `LICENSE`.
