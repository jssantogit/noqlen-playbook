# Noqlen Playbook

Noqlen Playbook is a lightweight operating guide for AI-assisted software work across the Noqlen ecosystem.

Its goal is simple: **move quickly without giving up evidence, safety, or reviewability**.

The playbook is intentionally risk-based. Low-risk work should be cheap to execute. Extra process appears only when a concrete risk, uncertainty, or hard-to-reverse decision justifies it.

## Core Loop

```text
Inspect -> Implement -> Verify -> Review
```

This is a working method, not a required response format. **Do the work; do not narrate the process.** Do not output step headings, gate status, risk tiers, Tool Mode, context levels, or similar process metadata merely to prove compliance.

### Inspect

Understand the requested behavior and the smallest relevant part of the repository before editing. Read more context only when the change requires it.

### Implement

Make the smallest **complete and coherent** change that satisfies the request. Avoid unrelated refactors and speculative abstractions. Do not keep a diff artificially small at the cost of correctness or maintainability.

### Verify

Run validation proportional to the behavior changed. Use the cheapest evidence that can realistically catch the likely regression. Never claim completion without evidence. If validation cannot run, report the reason and residual risk.

### Review

Inspect the actual diff, confirm the requested behavior is covered, check for scope drift, and make sure no new risk was introduced.

## Triggered Escalations

The core loop is always used. Escalate only when a concrete condition changes how the work should be approached:

- **Plan** — planning can materially change what is built, where it belongs, or the order of implementation.
- **Design** — a durable architectural decision, strategy, or boundary is meaningfully hard to reverse.
- **Safety** — real execution can materially harm data, users, security, repository history, production, or published state.
- **Audit** — independent scrutiny materially reduces a high-impact residual risk that normal validation plus diff review may not adequately catch.

Do not enumerate inactive escalations and do not create an artifact merely to prove one was considered.

See [`docs/workflow.md`](docs/workflow.md) for decision rules.

## Supporting Rules

- **Isolation Rule** — isolate external, unsafe, nondeterministic, expensive, slow, or CI-unavailable dependencies during verification using the lightest useful fixture, stub, fake, emulator, temporary state, or deterministic substitute.
- **Handoff Trigger** — persist a handoff only when work is interrupted/transferred and repository state alone is insufficient for safe continuation.

Neither rule must be declared in routine output.

## Principles

- Use the smallest safe context.
- Prefer executable guardrails over repeated prompt warnings.
- Validate before claiming done.
- Review the actual diff, not only the agent summary.
- Keep changes focused; do not rewrite unrelated code opportunistically.
- Use risk-based testing.
- Use synthetic fixtures instead of real private libraries or user data.
- Implement and test dangerous capabilities safely in isolated state; require explicit apply intent before performing high-impact actions against real state when not already authorized.
- Use dry-run or preview behavior before destructive real-state operations when practical.
- Never expose secrets, credentials, personal paths, private data, lyrics, fingerprints, or real music-library data.
- Keep heavy domain logic out of UI screens and thin app shells.
- Create abstractions for product or architectural reasons, not merely to satisfy a testing ritual.
- Never create an interface only so a fake can exist.
- Use ADRs only for decisions that are architectural and meaningfully hard to reverse.
- Diff size alone is not a reason for formal audit.

## Documentation Map

Read only what the task needs:

- [`docs/workflow.md`](docs/workflow.md) — core loop, escalations, Isolation Rule, and Handoff Trigger.
- [`docs/safety.md`](docs/safety.md) — destructive operations, private data, repository hygiene, security boundaries.
- [`docs/testing.md`](docs/testing.md) — risk-based validation, isolation, fixtures, fakes, and dry-run testing.
- [`docs/architecture.md`](docs/architecture.md) — boundaries, public APIs, dependencies, ADR criteria.
- [`docs/release.md`](docs/release.md) — release preparation and publishing controls.
- [`docs/tooling.md`](docs/tooling.md) — optional agent/tooling guidance; tooling is not part of the core workflow.

## Conditional Templates

Templates are optional artifacts used only when they preserve information that would otherwise be expensive or unsafe to rediscover:

- [`templates/change-brief.md`](templates/change-brief.md) — when Plan is active and a durable written brief materially reduces ambiguity or coordination cost.
- [`templates/adr/adr-template.md`](templates/adr/adr-template.md) — when Design produces a hard-to-reverse architectural decision worth preserving.
- [`templates/handoff.md`](templates/handoff.md) — when the Handoff Trigger fires because work is interrupted or transferred.

Do not create a template artifact when repository state, the task description, and validation evidence are already sufficient.

## Git And Repository Safety

- Do not force push or rewrite history unless explicitly requested.
- Do not publish, deploy, merge, or release unless the user requested that action.
- Prefer explicit staging over broad staging when working interactively.
- Keep local agent configuration, credentials, generated state, and personal paths out of the repository.

## Validation

For this repository:

```bash
python3 scripts/validate_playbook_structure.py
python3 scripts/check_repo_contamination.py
```

If `python3` is unavailable, use `python` and report the fallback.

The structure validator checks the small set of V2 essentials. It does not require historical process files merely because they once existed.
