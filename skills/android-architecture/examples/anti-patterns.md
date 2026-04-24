# Architecture Anti-Patterns (Examples)

## 1) God ViewModel

Bad:
- ViewModel handles networking, mapping, persistence, and UI state.

Better:
- ViewModel coordinates UI state and use cases.
- Data operations remain in data/domain boundaries.

## 2) Fake modularization

Bad:
- Dozens of tiny modules with unclear ownership and no build gain.

Better:
- Modules split by feature ownership, release cadence, or dependency boundary value.

## 3) Feature-to-feature coupling

Bad:
- `feature-payments` directly imports `feature-profile`.

Better:
- Shared contracts live in domain/core modules.
- Features communicate through navigation/events/contracts, not direct implementation deps.
