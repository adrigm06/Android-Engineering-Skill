# Android Engineering Skill Regression Prompts

Use these prompts to verify behavior consistency after skill changes.

## Instructions

1. Run each prompt in a fresh conversation.
2. Save each response as `responses/Pxx.md`.
3. Score responses with `evaluation-rubric.md` or `run_regression.py`.

## Prompt Suite

### P01 - Greenfield architecture
Design the architecture for a personal finance Android app for 8 developers, using Compose, offline sync, and biweekly releases.

### P02 - Legacy migration
We have a legacy Android app with coupled modules and XML UI. Propose an incremental migration to Compose without stopping feature delivery.

### P03 - Compose state model
Review this approach: one ViewModel with many mixed states and events. How should I restructure it for Compose?

### P04 - Jank diagnosis
I have jank on a list screen with filters and animations. Give me a diagnosis and optimization plan.

### P05 - Gradle build performance
Our clean build takes 11 minutes and CI is unstable. Propose a phased Gradle improvement plan.

### P06 - Testing strategy under deadline
Define a testing strategy for checkout and payments in Android with a small team and aggressive deadline.

### P07 - Flaky test reduction
We have 18 percent flaky UI tests. How do we reduce this in two sprints without delaying release?

### P08 - Security controls
We store tokens in SharedPreferences and only partial certificate pinning is enabled. Assess risk and remediation plan.

### P09 - Release go/no-go
Crash rate increased from 0.4 percent to 1.2 percent in release candidate. Go or no-go? Define rollout and rollback.

### P10 - Intermittent debugging
There is an intermittent crash on Android 13 when returning from background, not always reproducible.

### P11 - Cross-domain conflict
To improve startup, I want to temporarily break an architecture boundary. Is it acceptable?

### P12 - Structured code review
Perform an Android PR review focused on security, performance, and maintainability.

### P13 - Startup MVP tradeoffs
We are a startup with three developers and need to launch in four weeks. What technical debt is acceptable and how do we control it?

### P14 - Enterprise governance
Enterprise Android app with compliance requirements and five parallel teams. Define technical governance.

### P15 - Ambiguous optimization request
Optimize the whole Android app.
