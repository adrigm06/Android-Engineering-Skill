# Compose State Patterns

## Screen state model

Prefer a single immutable UI state type per screen:

- Loading
- Content(data)
- Empty
- Error(message, retry)

## State hoisting

Hoist to:

- Screen-level state holder for domain-backed state
- Reusable composable local state for ephemeral UI-only concerns

## Recomposition checklist

- Are parameters stable?
- Are expensive computations memoized where needed?
- Are list keys stable?
- Are side effects isolated with proper effect APIs?
- Are lambdas recreated unnecessarily in hot paths?
