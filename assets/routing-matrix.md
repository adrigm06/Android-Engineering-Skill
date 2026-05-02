# Android Skill Routing Matrix

Pick one lead skill. Add only supporting skills with material impact.

| Request pattern | Lead skill | Typical supporting skills |
|---|---|---|
| App structure, modularization, migration strategy | `android-architecture` | `android-gradle-build`, `android-testing`, `android-security` |
| Compose state, recomposition, UI architecture | `android-compose` | `android-performance`, `android-architecture`, `android-testing` |
| Build time, CI throughput, Gradle structure | `android-gradle-build` | `android-architecture`, `android-release-engineering`, `android-testing` |
| Test strategy, flakiness, coverage ROI | `android-testing` | `android-release-engineering`, `android-architecture`, `android-performance` |
| Startup/jank/ANR/memory/battery | `android-performance` | `android-compose`, `android-architecture`, `android-release-engineering` |
| Secrets, storage/network hardening, exploitability | `android-security` | `android-architecture`, `android-release-engineering` |
| PR review and tech debt assessment | `android-code-review` | Domain skills based on findings |
| Intermittent bugs and root-cause analysis | `android-debugging` | `android-performance`, `android-architecture`, `android-security` |
| Go/no-go, rollout/rollback policy | `android-release-engineering` | `android-security`, `android-performance`, `android-testing` |

## Arbitration reminders

- Critical exploitability risk -> `android-security` override.
- Production go/no-go and rollback policy -> `android-release-engineering` override.
- Structural boundaries -> `android-architecture` authority.
- Runtime SLA constraints -> `android-performance` authority.

Use `../AGENTS.md` as final policy authority.

## Lead skill tiebreaker (multi-domain tasks)

When multiple domains match, select lead by this priority:

1. If exploitability or sensitive data is at risk → `android-security` (critical override)
2. If a go/no-go or rollback decision is blocking → `android-release-engineering`
3. If the dominant structural question is about module/layer design → `android-architecture`
4. If the dominant runtime question is about startup/jank/ANR/memory → `android-performance`
5. If the dominant question is about build/CI correctness → `android-gradle-build`
6. If the dominant question is about coroutine/Flow correctness → `android-kotlin-concurrency`
7. Otherwise → lead is the domain with the highest user-stated concern
