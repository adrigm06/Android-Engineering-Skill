# Android Engineering Skill Package

A modular, composable, open-source skill system for Android engineering tasks.

This repository is designed for agentic workflows where skills are loaded by context.
It is intentionally structured to behave like a senior Android Staff Engineer rather than a generic coding assistant.

## Why this repository exists

Most Android "assistant prompts" become monolithic and hard to maintain.
This package takes a different approach:

- Global engineering policy in `AGENTS.md`
- Focused domain skills in `skills/*`
- Reusable references, templates, and examples
- Decision-oriented outputs with tradeoffs and risks

## Design goals

- Real modularity across skills
- Clear architecture boundaries and dependency rules
- Practical recommendations over architecture dogma
- Open-source maintainability and contribution friendliness
- Extensible foundation for future tooling and MCP integrations

## Non-goals

- A single giant prompt for all Android topics
- Framework-agnostic generic advice
- Tooling lock-in to one CI/CD vendor
- "One true architecture" prescriptions without context

## Repository layout

```text
AGENTS.md                  # Always-on rules for all skills
CONTEXT.md                 # Design contract for this package
skills/<skill-name>/       # Specialized domain skills
  SKILL.md                 # Triggering + workflow + output contract
  references/              # Deep guidance and decision trees
  templates/               # Reusable output templates
  examples/                # Good vs bad patterns
```

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

## Usage model

1. Keep `AGENTS.md` loaded as passive global context.
2. Load only the skill(s) relevant to the user task.
3. Return structured outputs with explicit tradeoffs.
4. Escalate to additional skills only when needed.

## Output quality baseline

Every recommendation should include:

- What to do
- Why this choice is preferred
- Main alternatives
- Risks and mitigations
- Practical next steps

## Contributing

See `CONTRIBUTING.md` for contribution standards and review expectations.

## Security

See `SECURITY.md` for vulnerability reporting.

## License

MIT License. See `LICENSE`.
