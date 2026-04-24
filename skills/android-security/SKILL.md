---
name: android-security
description: Android security engineering skill for threat-aware recommendations on secrets handling, secure storage, network hardening, Play Integrity, and release safeguards. Use this whenever security posture or sensitive data handling is in scope.
---

# Purpose

Provide practical Android security guidance with realistic threat awareness and implementation boundaries.

## When to use

- Handling credentials, tokens, keys, or sensitive user data
- Hardening network communication and API trust boundaries
- Reviewing secure storage decisions
- Designing app integrity and tamper resistance controls
- Security review of architecture/build/release flows

## Principles

1. Minimize sensitive data exposure by design.
2. Apply least privilege and shortest viable retention.
3. Keep secrets out of source control and artifacts.
4. Prefer platform-backed secure primitives over custom crypto.
5. Align mitigations with realistic threat models and costs.

## Workflow

1. Identify assets and trust boundaries.
2. Map likely threats and attack surfaces.
3. Propose layered mitigations.
4. Validate implementation feasibility and operational cost.
5. Prioritize fixes by severity and exploitability.
6. Produce rollout and verification checklist.

## Output format

1. `Risk summary`
2. `Threat surfaces`
3. `Mitigation plan`
4. `Storage/network/integrity controls`
5. `Residual risks`
6. `Implementation priorities`

## Rules and restrictions

- Do not suggest hardcoded secrets or token logging.
- Do not recommend custom cryptography when platform APIs suffice.
- Do not treat certificate pinning as universal; apply contextually.
- Do not claim absolute client-side tamper prevention.

## Anti-pattern detection

- Secrets in source, resources, or Gradle files
- Plaintext local persistence of sensitive data
- Missing TLS hardening and trust validation
- Security checks that exist only in UI layer

## Related resources

- `references/mobile-threat-model.md`
