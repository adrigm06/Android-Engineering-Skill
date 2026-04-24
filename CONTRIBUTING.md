# Contributing

Thanks for contributing to the Android Engineering Skill Package.

## Contribution principles

- Keep skills focused on one domain
- Move shared rules to `AGENTS.md`
- Prefer explicit decision criteria over generic tips
- Add anti-pattern detection and failure modes
- Keep outputs structured and actionable

## Repository conventions

### Skill structure

```text
skills/<skill-name>/
  SKILL.md
  references/   (optional but recommended for depth)
  templates/    (optional, for reusable outputs)
  examples/     (optional, for good/bad contrast)
```

### Naming

- Use kebab-case directory names: `android-architecture`
- Match frontmatter `name` with directory name

## Pull request checklist

Before opening a PR:

- [ ] Scope is clear and limited
- [ ] No duplicated global rules
- [ ] SKILL.md includes trigger conditions, workflow, output format, anti-patterns
- [ ] References/templates/examples are coherent and not redundant
- [ ] Language is practical and non-dogmatic
- [ ] Markdown formatting is clean

## Suggested PR format

- Problem
- Proposed change
- Tradeoffs
- Example prompt(s)
- Expected output shape

## Reporting issues

Open an issue with:

- Skill name(s) involved
- Reproducible prompt
- Current behavior
- Expected behavior
- Why it matters (risk, quality, maintainability, etc.)
