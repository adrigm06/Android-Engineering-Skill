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

---

## Worked examples

### Example A — Startup / Greenfield

```
Product maturity: greenfield
Release cadence: weekly
Deadline pressure: high
Team: 3 engineers, single ownership zone
UI stack: Compose (starting fresh)
Architecture: MVVM + single module (starting)
Build: default Android Gradle, no CI yet
Security: user auth (Google Sign-In), no PII
Performance baselines: none
Requested mode: Generation
Output depth: standard
Risk profile: balanced
```

**→ Lead skill:** `android-architecture` (greenfield structure decision dominates)
**→ Supporting:** `android-gradle-build` (CI setup), `android-testing` (initial strategy)
**→ Mode:** Generation
**→ Confidence starting point:** Medium — no existing constraints to validate against; architecture choices are reversible

---

### Example B — Enterprise / Legacy Modernization

```
Product maturity: legacy-heavy
Release cadence: biweekly
Deadline pressure: medium
Team: 15 engineers, 4 feature teams + 1 platform team
UI stack: XML + Compose hybrid (migrating)
Architecture: MVVM in monolith, multiple boundary violations
Module graph: single app module, 3 lib modules
Build: Gradle 7, kapt everywhere, 12-min clean builds
Security: payments + PII, PCI-adjacent compliance
Performance baselines: startup ~4s cold (internal traces)
Requested mode: Design
Output depth: deep
Risk profile: conservative
```

**→ Lead skill:** `android-architecture` (migration strategy dominates)
**→ Supporting:** `android-security` (compliance gates), `android-gradle-build` (build pain is concrete), `android-testing` (migration confidence)
**→ Mode:** Design
**→ Confidence starting point:** Medium — boundary violations known, but dependency graph details needed to finalize module extraction order

