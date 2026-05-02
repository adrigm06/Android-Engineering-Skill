# Android Project Context Assessment

Use this before selecting lead and supporting skills.

## 1) Product and delivery context

- Product maturity: `greenfield | scaling | legacy-heavy | enterprise | startup-mvp`
- Release cadence: `daily | weekly | biweekly | monthly | ad-hoc`
- Deadline pressure: `high | medium | low`

## 2) Team and ownership

- Team size and topology
- Ownership boundaries (feature/domain/platform)
- Current coordination pain points

## 3) Technical baseline

- UI stack: Compose/XML/hybrid
- Architecture style in use: MVVM/MVI/UDF/Clean depth
- Module graph shape and known boundary violations
- Data/network stack and offline requirements
- Build and CI constraints (time, cache reliability, flakiness)

## 4) Risk and compliance posture

- Sensitive data handling scope (tokens, PII, regulated data)
- Security or compliance requirements
- Critical user journeys and failure impact

## 5) Evidence availability

- Performance baselines/traces available?
- Test and flakiness baselines available?
- Crash/ANR/release metrics available?

## 6) Decision output requirements

- Requested mode: `Design | Review | Generation | Debug`
- Required output depth: `quick | standard | deep`
- Acceptable risk profile: `conservative | balanced | aggressive`

## Confidence note

If sections 3-5 are incomplete, continue with explicit assumptions and lower confidence.
