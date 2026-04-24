---
name: android-code-review
description: Structured Android code review skill with severity-based findings across architecture, correctness, maintainability, performance, and security. Use this for PR reviews and technical debt assessments.
---

# Purpose

Run disciplined Android code reviews with clear severity, evidence, and fix guidance.

## When to use

- Reviewing pull requests
- Auditing module quality and architecture drift
- Prioritizing technical debt fixes

## Workflow

1. Understand scope and intent of changes.
2. Evaluate architecture and dependency boundaries.
3. Check correctness and maintainability risks.
4. Check performance and security implications.
5. Return prioritized findings and concrete fixes.

## Output format

1. `Findings by severity`
2. `Evidence`
3. `Risk/impact`
4. `Recommended fix`
5. `Suggested follow-up checks`

## Anti-pattern detection

- Hidden architectural coupling
- Overly broad APIs and unclear ownership
- Missing tests on critical behavior changes
- Performance regressions in hot paths
