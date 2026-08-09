# Testing

Verification is always required. Test depth is proportional to the changed behavior and failure impact.

## Risk-Based Validation

Use the cheapest evidence that can realistically catch regressions for the change.

Typical progression:

- docs/config wording: structure checks, parser/lint checks, or direct review;
- local deterministic logic: focused unit tests;
- multi-module behavior: integration tests plus focused unit coverage;
- public boundary: contract/compatibility tests when the boundary matters to consumers;
- file/data/security behavior: positive and negative cases, path/boundary checks, dry-run evidence;
- release: broad test suite plus release-readiness checks.

Do not run a massive suite by ritual when a targeted check gives sufficient evidence. Do not skip broader checks when blast radius is real.

## Regression Rule

When changed behavior is important enough that a future regression would matter, prefer a durable automated test.

A test should prove behavior, not implementation trivia.

## Synthetic Data First

Automated tests must not depend on a real user's music library, credentials, private files, personal paths, or provider state.

Prefer:

- temporary directories;
- synthetic metadata;
- sanitized fixtures;
- deterministic clocks/randomness;
- local emulators;
- fake or stub providers where appropriate.

## Isolation Rule

Isolation is a verification technique, not a workflow phase or gate that must be declared.

Isolate the real dependency when exercising it directly would be:

- unsafe;
- external;
- nondeterministic;
- slow or expensive;
- flaky;
- unavailable in CI;
- dependent on real user data or state.

Use the lightest useful substitute: fixture, stub, fake, emulator, temporary directory, deterministic clock/random source, or an injected dependency when a real boundary already exists.

Examples include network providers, filesystem operations over real libraries, subprocesses, clocks, external services, and hardware.

### Anti-pattern

Do not create `SomethingProvider` plus `FakeSomethingProvider` merely because testing guidance mentions isolation.

Create an abstraction when the product or architecture benefits from a stable boundary. Once that boundary exists, use the lightest test double needed to test consumers safely.

A temporary directory or fixture is often enough; do not promote a simple test need into a new architectural surface.

## Dry-Run Testing

Operations that move, delete, overwrite, import, publish, migrate, or clean real data should expose preview/dry-run behavior when practical.

Tests should confirm that preview:

- identifies the same target set apply would use;
- does not mutate real state;
- reports unsafe or ambiguous targets clearly;
- prevents traversal or boundary escape where paths are involved.

Implementation and tests should exercise these behaviors on isolated state. User confirmation is about applying high-impact behavior to real state, not about running safe tests.

## Failure Evidence

If validation fails:

- preserve enough raw failure detail to diagnose the issue;
- do not replace the failure with a vague summary;
- fix or clearly report residual risk before claiming completion.

Compressed command output is fine during exploration as long as it does not hide the evidence needed to understand a failure.
