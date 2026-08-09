# Workflow

The Noqlen workflow has one universal loop:

```text
Inspect -> Implement -> Verify -> Review
```

Everything else is conditional.

## Operating Rule: Do The Work, Do Not Narrate The Process

The workflow is a way to work, not a required response format.

Do not output `Inspect`, `Implement`, `Verify`, `Review`, gate status, risk tier, Tool Mode, context level, or other process metadata merely to prove the workflow was followed.

Report process details only when they materially help the user or reviewer understand a decision, a safety constraint, validation evidence, a blocker, or residual risk.

Do not enumerate inactive gates.

## 1. Inspect

Before editing:

- understand the requested behavior;
- locate the smallest relevant code or documentation surface;
- identify existing tests and boundaries;
- notice operations that could affect real data, public contracts, security, repository history, production, or release state.

Do not pre-load broad architecture history by default. Expand context only when the task cannot be understood safely from the relevant code, tests, and nearby docs.

## 2. Implement

Make the smallest **complete and coherent** change that satisfies the task.

Default behavior:

- follow existing patterns;
- avoid unrelated cleanup;
- avoid speculative abstractions;
- keep edits reviewable as one logical change;
- stop expanding scope when a newly discovered issue is not required for the requested behavior.

Do not keep a diff artificially small at the cost of correctness, maintainability, or a complete solution.

A task does not need a written spec merely because it changes code or touches several files.

## 3. Verify

Validation is mandatory; its depth is risk-based.

Use the cheapest evidence that can realistically catch the likely regression.

Examples:

- documentation edit: structure/link checks or direct review may be enough;
- local deterministic logic: targeted unit tests plus relevant broader tests when blast radius warrants them;
- integration boundary: contract/integration tests with isolated dependencies;
- destructive/data/security behavior: targeted tests, negative cases, dry-run evidence, and broader validation;
- release: full release-readiness checks.

If a useful test does not exist and the behavior is important enough to regress, add one.

See the **Isolation Rule** below when the real dependency is unsafe, nondeterministic, expensive, slow, or unavailable in CI.

## 4. Review

Review the actual diff after validation.

Check:

- requested behavior is implemented;
- no unrelated files or behavior changed;
- tests match the changed behavior;
- error handling and boundaries still make sense;
- no secrets/private data/local configuration leaked;
- no unnecessary abstraction or compatibility surface was introduced;
- any activated escalation was satisfied.

Formal audit is not the default. Diff review is.

---

# Triggered Escalations

Escalate only when a concrete condition changes how the work should be approached. Do not classify every task into a process tier and do not create artifacts merely to prove an escalation was considered.

The four escalations are **Plan, Design, Safety, and Audit**.

## Plan

Plan before implementation when planning can materially change **what is built, where it belongs, or the order in which it should be built**.

Typical triggers:

- requirements are ambiguous in a way that changes behavior or acceptance;
- multiple plausible implementation approaches have meaningful trade-offs;
- ownership or placement is unclear, such as core versus app or one repository versus another;
- several independent components must coordinate through an interface or sequence that is not already established;
- decomposition is needed because implementing directly would create avoidable rework or an unreviewable change.

Do **not** activate Plan merely because a task touches many files, looks large, or feels complex if inspection already reveals a clear implementation path.

Output can be conversational. Use `templates/change-brief.md` only when a durable written brief materially reduces ambiguity or coordination cost.

## Design

Activate when the work makes a durable architectural decision that is expensive to reverse or important for future consumers.

Typical triggers:

- public API **strategy**, compatibility policy, or versioning direction;
- persistent storage/schema strategy;
- a new runtime dependency with meaningful long-term maintenance, security, packaging, or operational cost;
- app/core, service, or repository boundary strategy;
- authentication/security architecture;
- cross-repository contracts that independent consumers will rely on.

A routine edit to an existing public API does not automatically activate Design. The escalation is about changing the **strategy or durable boundary**, not every surface-level API modification.

Use an ADR when the decision should remain discoverable after the implementation context disappears.

Do not write ADRs for ordinary implementation choices.

## Safety

Activate when the work introduces or changes behavior whose **real execution** can materially harm data, users, repository history, production state, credentials, or published artifacts.

Typical triggers:

- delete, move, overwrite, import, migrate, or publish real data;
- authentication, authorization, secrets, or security controls;
- production/deployment actions;
- force push, history rewrite, destructive cleanup;
- use of real private libraries or user datasets;
- release publication.

**Implementing or testing a destructive capability against synthetic data, temporary directories, mocks, or isolated state does not itself require user confirmation.** Confirmation is required before the agent performs a destructive, publishing, production, or otherwise high-impact action against real state when that action is not already explicitly authorized.

The escalation may require dry-run/preview behavior, backup/recovery notes, stronger tests, restricted permissions, a reversible staging environment, or explicit apply intent. Use only controls that map to a concrete failure mode. See `docs/safety.md`.

## Audit

Activate when independent or formal review materially reduces a **high-impact residual risk** that normal validation plus diff review may not adequately catch.

Typical triggers:

- security-sensitive changes;
- release readiness;
- high-impact data operations;
- important public API strategy or app/core boundary changes;
- migrations with difficult rollback;
- changes where a plausible failure has material consequences despite passing normal tests.

**Diff size alone does not activate Audit.** A large mechanical change with strong deterministic validation can be lower risk than a five-line authorization change.

Prefer an independent/read-only reviewer when available. The implementer summarizing their own work is not a substitute for independent scrutiny when Audit is triggered.

For normal work, targeted validation plus diff review is sufficient.

---

# Supporting Rules

These rules support the core loop but are not gates that must be declared or reported.

## Isolation Rule

When exercising the real dependency would be unsafe, nondeterministic, slow, expensive, flaky, unavailable in CI, or dependent on real user state, isolate it during verification.

Useful isolation techniques include:

- fixtures;
- stubs;
- fakes;
- emulators;
- temporary directories;
- deterministic clocks/randomness;
- dependency injection where a real boundary already benefits from it.

Use the lightest technique that provides meaningful evidence.

**Do not create an interface only so a fake can exist.** A boundary should exist because the product or architecture needs it. Testing then isolates that real boundary.

See `docs/testing.md`.

## Handoff Trigger

Persist a handoff only when continuity cannot safely rely on repository state alone:

- session/context is ending before the task is complete;
- work moves to another agent or person;
- an external blocker pauses implementation;
- important uncommitted assumptions or next steps would otherwise be lost.

Use `templates/handoff.md` as a compact checkpoint.

Do not write a handoff after every completed task or block.

---

# Decision Examples

### Rename a label in one screen

Core loop only. No spec, fake, audit report, Tool Mode, gate-status report, or handoff.

### Add deterministic sorting to an existing list

Core loop. Add/update tests if the behavior can regress. No isolation technique is needed unless sorting crosses a real external boundary.

### Add a new provider API behind an existing service boundary

Core loop + Isolation Rule for tests. Use Plan only if provider behavior or integration direction is genuinely unclear. Use Design only if the durable public boundary or compatibility strategy changes.

### Implement a delete-duplicates feature using temporary test directories

Core loop + Safety-aware design and Isolation Rule. No user confirmation is needed merely to implement or test the capability in isolated state. Confirmation/apply intent is required before deleting real user files.

### Change persistent metadata schema

Core loop + Design + Safety. Add Audit when migration failure could have material consequences that normal tests/review may not adequately catch.

### Delete duplicate files from a real library

Core loop + Safety. Use isolated temporary data for automated tests. Dry-run/preview and recovery strategy are expected before apply behavior.

### Prepare a release

Core loop + Safety + Audit. Publishing remains a separate explicit action.

---

# Prompt Guidance

A normal implementation prompt should contain only what the agent needs now:

- task;
- relevant constraints/invariants not already discoverable in the repository;
- acceptance criteria when they are not obvious;
- validation expectations if project defaults are insufficient.

Do not repeat the same goal/scope/allowed-files/forbidden-files/validation/stop-condition data across multiple artifacts unless a concrete risk makes that duplication useful.

Do not add a workflow preamble or gate-status checklist to routine work.

Prefer repository-enforced permissions, tests, CI, branch isolation, and tool restrictions over long repeated warning prose.
