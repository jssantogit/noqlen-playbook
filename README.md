# Noqlen Playbook

Noqlen Playbook is a lightweight operating guide for AI-assisted software work across the Noqlen ecosystem.

Its goal is simple: **move quickly without giving up evidence, safety, or reviewability**.

The playbook is intentionally risk-based. Low-risk work should be cheap to execute. Extra process appears only when a concrete risk or irreversible decision justifies it.

## Core Loop

```text
Inspect -> Implement -> Verify -> Review
```

### Inspect

Understand the requested behavior and the smallest relevant part of the repository before editing. Read more context only when the change requires it.

### Implement

Make the smallest coherent change that satisfies the request. Avoid unrelated refactors and preserve existing boundaries unless changing them is part of the task.

### Verify

Run validation proportional to the behavior changed. Never claim completion without evidence. If validation cannot run, report the reason and residual risk.

### Review

Inspect the diff, confirm the requested behavior is covered, check for scope drift, and make sure no new risk was introduced.

## Triggered Gates

The core loop is always used. The following gates are **conditional**:

- **Plan Gate** — use when requirements are ambiguous, several subsystems are involved, or the implementation path is uncertain.
- **Design Gate** — use for hard-to-reverse architecture, public API strategy, storage/schema changes, new dependencies, or important app/core boundaries.
- **Safety Gate** — use for destructive operations, real user data, authentication/security, migrations, publishing, production actions, or other high-impact changes.
- **Fake Gate** — use when an external, expensive, nondeterministic, or unsafe dependency benefits from isolation in tests or development.
- **Audit Gate** — use for security-sensitive work, releases, risky data operations, important public boundaries, or changes where independent review adds material value.
- **Handoff Gate** — use when work is interrupted, transferred to another agent/session, or cannot be safely resumed from repository state alone.

A gate exists because of a concrete condition, not because every task must fill a template.

See [`docs/workflow.md`](docs/workflow.md) for decision rules.

## Principles

- Use the smallest safe context.
- Prefer executable guardrails over repeated prompt warnings.
- Validate before claiming done.
- Review the actual diff, not only the agent summary.
- Keep changes focused; do not rewrite unrelated code opportunistically.
- Use risk-based testing.
- Use synthetic fixtures instead of real private libraries or user data.
- Use dry-run or preview behavior before destructive operations when practical.
- Never expose secrets, credentials, personal paths, private data, lyrics, fingerprints, or real music-library data.
- Keep heavy domain logic out of UI screens and thin app shells.
- Create abstractions for product or architectural reasons, not merely to satisfy a testing ritual.
- Never create an interface only so a fake can exist.
- Use ADRs only for decisions that are architectural and meaningfully hard to reverse.

## Documentation Map

Read only what the task needs:

- [`docs/workflow.md`](docs/workflow.md) — core loop and gate decisions.
- [`docs/safety.md`](docs/safety.md) — destructive operations, private data, repository hygiene, security boundaries.
- [`docs/testing.md`](docs/testing.md) — risk-based validation, fixtures, fakes, dry-run testing.
- [`docs/architecture.md`](docs/architecture.md) — boundaries, public APIs, dependencies, ADR criteria.
- [`docs/release.md`](docs/release.md) — release preparation and publishing controls.
- [`docs/tooling.md`](docs/tooling.md) — optional agent/tooling guidance; tooling is not part of the core workflow.

## Conditional Templates

Templates are optional artifacts activated by gates:

- [`templates/change-brief.md`](templates/change-brief.md) — Plan Gate when a short written design materially reduces ambiguity.
- [`templates/adr/adr-template.md`](templates/adr/adr-template.md) — Design Gate for hard-to-reverse architectural decisions.
- [`templates/handoff.md`](templates/handoff.md) — Handoff Gate for interrupted or transferred work.

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
