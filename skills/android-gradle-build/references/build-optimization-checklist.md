# Build Optimization Checklist

## Baseline first

Measure:

- Configuration time
- Incremental assemble time
- Clean build time
- Test task duration in CI

## Build layout

- `build-logic/` module for convention plugins
- `gradle/libs.versions.toml` for centralized versions
- Shared plugin IDs and Android defaults in conventions

## KSP vs kapt

Prefer KSP when ecosystem support is available.
Keep kapt only for processors not yet supported or migration-gated.

## CI essentials

- Enable Gradle build cache (local + remote where appropriate)
- Avoid non-cacheable custom tasks when possible
- Normalize environment differences to reduce cache misses
