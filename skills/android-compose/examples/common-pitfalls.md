# Common Compose Pitfalls

## Pitfall: Business logic in composable body

Risk:
- Hard to test, easy to break lifecycle assumptions.

Fix:
- Move logic to state holder/use case, render pure UI from state.

## Pitfall: Passing whole ViewModel to children

Risk:
- Hidden dependencies and recomposition sprawl.

Fix:
- Pass only state slice and event callbacks required by each child.

## Pitfall: Unbounded LazyColumn item recompositions

Risk:
- Jank in scroll-heavy screens.

Fix:
- Provide stable item keys, isolate item UI, avoid unstable models.
