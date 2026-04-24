---
name: android-code-review
description: Structured Android code review skill with severity-based findings across architecture, correctness, maintainability, performance, and security. Use this for PR reviews and technical debt assessments.
---

# Purpose

Run disciplined Android code reviews that prioritize issues by incident risk and provide implementation-ready fixes.

## Scope and authority

This skill is synthesis authority across domains.
It consolidates architecture, security, performance, testing, and release concerns into a prioritized outcome.

## When to use

- pull request reviews
- technical debt audits
- release-candidate quality checks

## Decision engine workflow

1. Establish change intent and blast radius.
2. Check non-negotiable constraints first.
3. Evaluate architecture, correctness, maintainability, performance, and security implications.
4. Rank findings by severity and operational impact.
5. Propose fix order and verification strategy.

## Branching decision tree

### Branch A: change risk profile

- `high blast radius` (cross-module, auth, payment, startup, release-critical):
  - perform deep multi-domain review with stricter evidence requirements
- `medium blast radius`:
  - prioritize correctness, maintainability, and boundary consistency
- `low blast radius`:
  - focus on local quality and regression prevention

### Branch B: release proximity

- `near release`:
  - prioritize regressions and production-risk findings first
- `normal window`:
  - include strategic maintainability improvements with staged follow-up

## Uncertainty protocol

Always include confidence on non-trivial findings.
For medium/low confidence findings, include the minimum evidence needed to confirm/refute.

## Output contract

Follow global order from `AGENTS.md`:

1. `Context and constraints`
2. `Decision and rationale`
3. `Alternatives considered`
4. `Tradeoffs`
5. `Risks and mitigations`
6. `Confidence and unknowns`
7. `Cross-skill impacts`
8. `Next implementation steps`

Then include review-specific artifacts:

- `Findings by severity`
- `Evidence`
- `Risk impact`
- `Recommended fix`
- `Follow-up checks`

## Anti-pattern detection

- hidden coupling or boundary violations
- missing tests on behavior-critical changes
- performance-sensitive changes with no measurements
- security-impacting changes with weak controls
