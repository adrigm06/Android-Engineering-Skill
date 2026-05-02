# Contributing

Thanks for contributing to the Android Engineering Skill Package.

This project is designed as a production-grade decision system, so contributions are reviewed for reasoning quality, not only formatting.

## Contribution philosophy

Contributions should improve at least one of:

- decision quality under constraints
- cross-skill coherence and conflict behavior
- real-world engineering fidelity
- contributor scalability and maintainability

Avoid contributions that only add checklist content without improving decision logic.

## Repository contracts by layer

- `AGENTS.md`: runtime constraints, authority model, arbitration protocol
- `CONTEXT.md`: product philosophy and mental model
- `skills/*/SKILL.md`: domain execution logic and branching
- `references/`, `templates/`, `examples/`: deep support artifacts

Do not duplicate global constraints inside every skill unless needed for local interpretation.

## Skill contribution requirements

Every new or changed `SKILL.md` must include:

- clear trigger scope and boundaries
- frontmatter `description` updated to clearly state what the skill does and when it should trigger
- explicit decision workflow (not flat checklist)
- context branching (if/then paths)
- uncertainty handling (`High/Medium/Low` confidence behavior)
- cross-skill interaction notes
- output aligned to global section order in `AGENTS.md`
- anti-pattern detection relevant to the domain
- corresponding catalog updates in `skills/README.md` (and `README.md` when user-facing behavior changes)

## Review gates for pull requests

A PR should pass these gates before merge:

1. **Constraint gate**: no conflict with non-negotiable runtime constraints.
2. **Authority gate**: no ambiguous ownership between skills.
3. **Composition gate**: cross-skill interactions are deterministic.
4. **Uncertainty gate**: medium/low confidence behavior is explicit.
5. **Output gate**: global output contract order is preserved.
6. **Realism gate**: recommendations reflect practical team constraints.

## PR checklist

Before opening a PR:

- [ ] Scope and rationale are explicit
- [ ] No duplicated global rules unless justified
- [ ] Skill changes include branching and tradeoff-aware logic
- [ ] Skill frontmatter `description` is updated and trigger intent is clear
- [ ] Uncertainty/confidence handling is defined
- [ ] Cross-skill implications are documented
- [ ] Output structure remains contract-compliant
- [ ] `skills/README.md` is updated when skill scope/behavior changes
- [ ] Markdown is clear and consistent
- [ ] `CHANGELOG.md` updated when behavior changes materially

## Suggested PR format

Use this structure in your PR description:

1. Problem and context
2. Decision and rationale
3. Alternatives considered
4. Risks and mitigations
5. Cross-skill impacts
6. Compatibility impact
7. Example prompt(s) and expected output shape

## Compatibility rules

- Keep skill names and trigger intent stable unless there is a strong reason to change.
- Avoid breaking output-contract or authority behavior without explicit migration notes.
- If a skill's decision behavior changes materially, document migration guidance in the PR.

## Issue reporting

When reporting issues, include:

- involved skill(s)
- reproducible prompt
- current vs expected behavior
- impact (safety, reliability, maintainability, performance, release risk)
- any relevant constraints (deadline, legacy, team size)

## Code of conduct and security

- Contributor behavior: `CODE_OF_CONDUCT.md`
- Security disclosures: open a private maintainer contact channel before public disclosure.
