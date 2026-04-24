# Android Engineering Skill Package - System Context

## Product intent

This repository is a professional, open-source Android engineering decision system.

It is designed for agentic usage where multiple specialized skills can be activated, composed, and resolved deterministically under production constraints.

The target behavior is not "generic advice," but senior-level decisions that balance safety, architecture quality, runtime reliability, delivery pressure, and team reality.

## Layer model and ownership

This package is intentionally split into three policy layers:

1. `AGENTS.md` - runtime rules, hard constraints, and global arbitration protocol.
2. `SKILL.md` files - execution logic per domain (decision trees, workflows, outputs).
3. `references/`, `templates/`, `examples/` - deep guidance and reusable artifacts.

Boundary contract:

- Keep non-negotiable constraints and arbitration only in `AGENTS.md`.
- Keep domain logic and branching only in each skill.
- Keep detailed supporting material in references/templates/examples.

## Mental model: decision engine, not checklist pack

Each skill is expected to operate as a context-sensitive decision engine:

- interpret constraints
- pick a strategy branch
- evaluate tradeoffs
- surface risks and uncertainty
- return actionable next steps

A skill should not emit fixed recommendations without context fit.

## System behavior in real-world ambiguity

The system must handle non-ideal conditions explicitly:

- incomplete or conflicting requirements
- legacy code and migration risk
- deadline and staffing constraints
- imperfect but defensible short-term choices

Recommendation quality is evaluated by decision quality under constraints, not by theoretical purity.

## Composition philosophy

Most non-trivial Android tasks span multiple domains.

Expected composition behavior:

- one lead skill for the dominant decision domain
- one or more supporting skills for constraints and side effects
- deterministic conflict resolution using the authority model from `AGENTS.md`
- one integrated answer with rejected options explained

## Skill quality standards

Every skill should:

- define clear triggers and boundaries
- include branching logic for context variants
- include uncertainty handling and confidence expectations
- include anti-pattern detection and failure modes
- produce outputs aligned with the global output contract order

## Engineering realism principles

To remain production-relevant, guidance should:

- include realistic tradeoffs (cost, speed, reliability)
- acknowledge when "not ideal" options are acceptable with mitigations
- separate temporary expedients from long-term target state
- provide migration sequencing with rollback-safe steps

## Evolution policy

The system evolves by increasing reasoning quality, composition robustness, and contributor scalability.

When adding or changing skills:

- preserve architecture and dependency constraints
- avoid rule duplication between global and skill scopes
- maintain backward compatibility for output contracts where possible
- document behavior changes with clear rationale and migration notes

## Scope

In scope:

- Android architecture and modularization
- Compose UI engineering
- Gradle/build and CI strategy
- testing, performance, security, debugging, code review, release

Out of scope:

- backend-only design not tied to Android implications
- generic guidance detached from Android runtime/build constraints

This document defines product philosophy and design intent.
Implementation rules belong in `AGENTS.md`, and domain execution belongs in each `SKILL.md`.
