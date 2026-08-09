# Workflow

The Noqlen workflow has one universal loop:

```text
Inspect -> Implement -> Verify -> Review
```

Everything else is conditional.

## 1. Inspect

Before editing:

- understand the requested behavior;
- locate the smallest relevant code or documentation surface;
- identify existing tests and boundaries;
- note any operation that could affect real data, public contracts, security, or release state.

Do not pre-load broad architecture history by default. Expand context only when the task cannot be understood safely from the relevant code, tests, and nearby docs.

## 2. Implement

Make the smallest coherent change that satisfies the task.

Default behavior:

- follow existing patterns;
- avoid unrelated cleanup;
- avoid speculative abstractions;
- keep edits reviewable as one logical change;
- stop expanding scope when a newly discovered issue is not required for the requested behavior.

A task does not need a written spec merely because it changes code.

## 3. Verify

Validation is mandatory; its depth is risk-based.

Examples:

- documentation edit: structure/link checks or direct review may be enough;
- local pure-function change: targeted unit tests plus relevant broader tests;
- integration boundary: contract/integration tests with isolated dependencies;
- destructive/data/security work: targeted tests, negative cases, dry-run evidence, and broader validation;
- release: full release-readiness checks.

If a useful test does not exist and the behavior is important enough to regress, add one.

## 4. Review

Review the actual diff after validation.

Check:

- requested behavior is implemented;
- no unrelated files or behavior changed;
- tests match the changed behavior;
- error handling and boundaries still make sense;
- no secrets/private data/local configuration leaked;
- no unnecessary abstraction or compatibility surface was introduced;
- any activated gate was satisfied.

Formal audit is not the default. Diff review is.

---

# Triggered Gates

A gate activates only when its condition is present. Do not classify every task into a process tier and do not create artifacts merely to prove the gate was considered.

## Plan Gate

Activate when one or more are true:

- the requested behavior is materially ambiguous;
- several independent modules or repositories must change together;
- there are multiple plausible approaches with meaningful trade-offs;
- the implementation path cannot be made clear by inspecting the relevant code;
- a large change would be difficult to review without decomposition.

Output can be conversational. Use `templates/change-brief.md` only when a durable written plan adds value.

Do not activate for straightforward local edits with obvious acceptance criteria.

## Design Gate

Activate for decisions that are architectural or expensive to reverse, including:

- public API strategy;
- persistent storage/schema strategy;
- new runtime dependency with meaningful long-term cost;
- app/core or service boundary changes;
- authentication/security architecture;
- cross-repository contracts that consumers will rely on.

Use an ADR when the decision should remain discoverable after the implementation context disappears.

Do not write ADRs for ordinary implementation choices.

## Safety Gate

Activate when work can materially harm data, users, repository history, production state, credentials, or published artifacts.

Typical triggers:

- delete, move, overwrite, import, migrate, or publish real data;
- authentication, authorization, secrets, or security controls;
- production/deployment actions;
- force push, history rewrite, destructive cleanup;
- use of real private libraries or user datasets;
- release publication.

The gate may require explicit confirmation, dry-run/preview behavior, backup/recovery notes, stronger tests, restricted permissions, or a reversible staging environment. See `docs/safety.md`.

## Fake Gate

Activate when an external or nondeterministic dependency makes direct testing unsafe, slow, expensive, flaky, or impractical.

Examples:

- network APIs;
- filesystem operations over real user data;
- clocks/randomness when determinism matters;
- subprocesses or services;
- paid providers;
- hardware or environment-specific integration.

Use the lightest useful test double: fixture, stub, fake, emulator, temporary directory, or dependency injection.

**Do not create an interface only so a fake can exist.** A boundary should exist because the product or architecture needs it. Testing then isolates that real boundary.

## Audit Gate

Activate when independent or formal review adds material safety value, such as:

- security-sensitive changes;
- release readiness;
- high-impact data operations;
- important public API or app/core boundary changes;
- migrations with difficult rollback;
- unusually large or high-risk diffs.

Prefer an independent/read-only reviewer when available. The implementer summarizing their own work is not a substitute for independent scrutiny when the gate is triggered.

For normal work, targeted validation plus diff review is sufficient.

## Handoff Gate

Activate when continuity cannot safely rely on repository state alone:

- session/context is ending before the task is complete;
- work moves to another agent or person;
- an external blocker pauses implementation;
- important uncommitted assumptions or next steps would otherwise be lost.

Use `templates/handoff.md` as a compact checkpoint.

Do not write a handoff after every completed task or block.

---

# Decision Examples

### Rename a label in one screen

Core loop only. No spec, fake, audit report, Tool Mode, or handoff.

### Add deterministic sorting to an existing list

Core loop. Add/update tests if the behavior can regress. No fake unless sorting crosses a real external boundary.

### Add a new provider API behind an existing service boundary

Core loop + Fake Gate. Plan Gate only if provider behavior or integration strategy is unclear. Design Gate only if the public boundary itself changes materially.

### Change persistent metadata schema

Core loop + Design Gate + Safety Gate. Add Audit Gate when migration impact is substantial.

### Delete duplicate files from a real library

Core loop + Safety Gate + Fake Gate for automated tests. Dry-run/preview and recovery strategy are expected before apply behavior.

### Prepare a release

Core loop + Safety Gate + Audit Gate. Publishing remains a separate explicit action.

---

# Prompt Guidance

A normal implementation prompt should contain only what the agent needs now:

- task;
- relevant constraints/invariants not already discoverable in the repository;
- acceptance criteria when they are not obvious;
- validation expectations if project defaults are insufficient.

Do not repeat the same goal/scope/allowed-files/forbidden-files/validation/stop-condition data across multiple artifacts unless a concrete risk makes that duplication useful.

Prefer repository-enforced permissions, tests, CI, branch isolation, and tool restrictions over long repeated warning prose.
