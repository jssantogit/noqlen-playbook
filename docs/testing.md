# Testing

Verification is always required. Test depth is proportional to the changed behavior and failure impact.

## Risk-Based Validation

Use the cheapest evidence that can realistically catch regressions for the change.

Typical progression:

- docs/config wording: structure checks, parser/lint checks, or direct review;
- local deterministic logic: focused unit tests;
- multi-module behavior: integration tests plus focused unit coverage;
- public boundary: contract/compatibility tests;
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

## Fake Gate

A fake is a tool, not a mandatory phase.

Use a fake, stub, fixture, emulator, or injected dependency when the real boundary is:

- external;
- nondeterministic;
- slow or expensive;
- unsafe to exercise repeatedly;
- unavailable in CI;
- dependent on real user data.

Examples include network providers, filesystem operations over real libraries, subprocesses, clocks, external services, and hardware.

### Anti-pattern

Do not create `SomethingProvider` plus `FakeSomethingProvider` merely because the workflow expects a fake.

Create an abstraction when the product or architecture benefits from a stable boundary. Once that boundary exists, use the lightest test double needed to test consumers safely.

## Dry-Run Testing

Operations that move, delete, overwrite, import, publish, migrate, or clean data should expose preview/dry-run behavior when practical.

Tests should confirm that preview:

- identifies the same target set apply would use;
- does not mutate real state;
- reports unsafe or ambiguous targets clearly;
- prevents traversal or boundary escape where paths are involved.

## Failure Evidence

If validation fails:

- preserve enough raw failure detail to diagnose the issue;
- do not replace the failure with a vague summary;
- fix or clearly report residual risk before claiming completion.

Compressed command output is fine during exploration as long as it does not hide the evidence needed to understand a failure.
