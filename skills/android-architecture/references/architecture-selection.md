# Architecture Selection Guide

## 1) Structure by team and product scale

| Context | Recommended shape | Why |
|---|---|---|
| Team <= 5, < 15 features | Modular monolith, package-by-feature | Lowest coordination cost, clear ownership |
| Team 6-15, 15-50 features | Selective multi-module (`feature-*`, `core-*`) | Better build isolation and boundaries |
| Multi-team, > 50 features | Strong multi-module + contract-first boundaries | Scales ownership and parallel delivery |

## 2) MVVM vs MVI/UDF

| Symptom | Prefer |
|---|---|
| Mostly CRUD screens and simple form logic | MVVM |
| Complex event flows and state transitions | MVI/UDF |
| Heavy Compose app with frequent recomposition concerns | UDF with immutable state |
| Legacy app with mixed patterns | Incremental MVVM cleanup first, then selective MVI |

## 3) Clean Architecture depth

Use deeper domain/data split when:

- Business rules are non-trivial
- Multiple data sources are expected to evolve
- Compliance/auditability needs are high

Keep it lighter when:

- Product is early and requirements are volatile
- Extra layers would be pass-through with no policy logic

## 4) Migration path from legacy

1. Stabilize boundaries around existing feature slices.
2. Isolate contracts in domain layer.
3. Move data-source implementation behind interfaces.
4. Split modules by ownership and build impact.
5. Remove temporary bridges once new boundaries hold.
