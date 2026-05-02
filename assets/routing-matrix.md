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
