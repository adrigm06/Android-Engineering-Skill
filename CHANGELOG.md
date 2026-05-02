# Changelog

All notable changes to this project are documented in this file.

## [Unreleased]

### Added

- Deterministic skill authority model in `AGENTS.md`.
- Cross-skill conflict resolution protocol and composition protocol in `AGENTS.md`.
- Global uncertainty and confidence protocol (`High/Medium/Low`) in `AGENTS.md`.
- Unified output contract with strict section order in `AGENTS.md`.
- Open-source issue templates under `.github/ISSUE_TEMPLATE/`.
- npm package scaffolding (`package.json`) with scoped `npx` installer entrypoint (`@adrigm06/android-engineering-skill`).
- Installer CLI at `bin/install-skill.js` to copy the skill package into a target directory.

### Changed

- `CONTEXT.md` refocused as product philosophy + layer ownership contract.
- `README.md` upgraded to explain system mental model and decision-engine behavior.
- `CONTRIBUTING.md` tightened with review gates and compatibility expectations.
- `skills/README.md` aligned with authority and composition model.
- Upgraded all skill contracts to include uncertainty handling and unified output expectations.
- Promoted `android-architecture`, `android-compose`, and `android-gradle-build` to explicit decision-engine style with branching logic and cross-skill conflict handling.
- `README.md` now documents `npx` installation usage.
- `CONTRIBUTING.md` security disclosure section updated after removing `SECURITY.md`.

### Compatibility notes

- Skill names remain stable.
- Global output contract order is explicit and mandatory for non-trivial outputs.

## [Initial]

### Added

- Initial open-source repository structure.
- Global policy files: `CONTEXT.md`, `AGENTS.md`.
- Core skills:
  - `android-architecture`
  - `android-compose`
  - `android-gradle-build`
  - `android-testing`
  - `android-performance`
  - `android-security`
- Additional operational skills:
  - `android-code-review`
  - `android-debugging`
  - `android-release-engineering`
- Supporting references, templates, and examples for core domains.
