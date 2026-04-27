# Review Severity and Evidence Guide

## Severity baseline

- `Critical`: exploitability, data loss, architecture breakage, release blocker
- `High`: high incident likelihood or major production impact
- `Medium`: meaningful risk with manageable blast radius
- `Low`: limited operational impact

## Minimum evidence per severity

- `Critical/High`:
  - concrete code evidence
  - risk path and affected scope
  - clear verification steps for fix
- `Medium/Low`:
  - concrete rationale and expected payoff

## Confidence rubric

- `High` (>= 0.80): strong evidence, low ambiguity
- `Medium` (0.60-0.79): partial evidence, notable assumptions
- `Low` (< 0.60): missing or conflicting evidence

For medium/low confidence findings, list what evidence could upgrade/downgrade severity.
