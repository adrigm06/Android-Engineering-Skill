# Module Boundaries and Dependency Direction

## Suggested baseline tree

```text
app/
core-common/
core-ui/
domain/
data/
feature-auth/
feature-home/
feature-settings/
design-system/
benchmark/
```

## Allowed dependencies

- `app -> feature-*`
- `feature-* -> domain`
- `feature-* -> core-common`
- `feature-* -> core-ui`
- `data -> domain`
- `design-system -> core-ui` (or inverse, but keep consistent)

## Forbidden dependencies

- `feature-a -> feature-b`
- `domain -> data`
- `domain -> app`
- `feature-* -> concrete data-source modules`

## API vs implementation guidance

- Expose module APIs only when another module needs compile-time contracts.
- Keep internal details behind `implementation` dependencies.
- Avoid turning every module into an API module by default.
