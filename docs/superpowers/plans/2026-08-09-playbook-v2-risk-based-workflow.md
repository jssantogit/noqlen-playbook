# Playbook V2 Risk-Based Workflow Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the ceremony-heavy Noqlen workflow with a smaller risk-based workflow that preserves validation, safety boundaries, and reviewability while removing redundant artifacts and token-heavy process metadata.

**Architecture:** The V2 playbook has one universal loop — Inspect -> Implement -> Verify -> Review — plus triggered gates for planning, design, safety, fakes, formal audit, and handoff. Durable safety rules live in `AGENTS.md`; detailed guidance is consolidated into a small set of focused docs; templates are reduced to artifacts that are created only when a gate is triggered.

**Tech Stack:** Markdown documentation, Python repository validation scripts, GitHub Actions.

## Global Constraints

- Preserve mandatory validation before claiming work complete.
- Preserve protection for secrets, private data, personal paths, real music libraries, destructive operations, and release actions.
- Do not require fake providers unless a real external or nondeterministic boundary benefits from isolation.
- Do not require Tool Mode or context-level declarations for normal work.
- Do not require formal audit or handoff after every block.
- ADRs remain reserved for hard-to-reverse architectural decisions.
- The final repository validator must check essential structure and hygiene, not historical file count.

---

### Task 1: Replace the canonical workflow

**Files:**
- Modify: `README.md`
- Modify: `AGENTS.md`
- Create: `docs/workflow.md`

**Interfaces:**
- Consumes: current safety principles and block discipline.
- Produces: the canonical V2 loop and gate definitions referenced by all remaining docs.

- [ ] Rewrite `README.md` around `Inspect -> Implement -> Verify -> Review`.
- [ ] Define triggered gates: Plan, Design, Safety, Fake, Audit, Handoff.
- [ ] State explicitly that gates are activated by concrete conditions, not by task labels or ritual.
- [ ] Reduce `AGENTS.md` to durable repository invariants and executable-safety expectations.
- [ ] Create `docs/workflow.md` with decision rules and examples of when each gate activates.
- [ ] Review the three files for duplicated rules and remove repetition.

### Task 2: Consolidate safety, testing, architecture, release, and tooling guidance

**Files:**
- Create: `docs/safety.md`
- Create: `docs/testing.md`
- Create: `docs/architecture.md`
- Create: `docs/release.md`
- Create: `docs/tooling.md`

**Interfaces:**
- Consumes: useful policy from the current testing, repo hygiene, app, audit, release, tooling, token-economy, and CI docs.
- Produces: five focused references that are read only when relevant.

- [ ] Move destructive-operation, private-data, repository-hygiene, and confirmation rules into `docs/safety.md`.
- [ ] Move risk-based validation, synthetic fixtures, dry-run testing, and conditional fakes into `docs/testing.md`.
- [ ] Move app/core boundaries, public API guidance, dependency decisions, and ADR criteria into `docs/architecture.md`.
- [ ] Move release-specific checks into `docs/release.md`.
- [ ] Move OpenCode/Serena/RTK/Context Mode/Caveman guidance into optional `docs/tooling.md` and remove Tool Mode from the canonical workflow.
- [ ] Ensure each document links back to the relevant gate rather than restating the entire workflow.

### Task 3: Replace redundant workflow artifacts with conditional templates

**Files:**
- Create: `templates/change-brief.md`
- Create: `templates/handoff.md`
- Retain/update: `templates/adr/adr-template.md`
- Remove obsolete context/spec/prompt templates that duplicate task scope, validation, audit, or tooling metadata.

**Interfaces:**
- Consumes: Plan/Design/Handoff gate definitions.
- Produces: one lightweight planning artifact, one continuation artifact, and one architectural-decision artifact.

- [ ] Create `change-brief.md` with Goal, Expected behavior, Constraints, Acceptance, Approach, and Risks.
- [ ] Create a compact `handoff.md` for interrupted work or session/agent transitions only.
- [ ] Simplify the ADR template to decision, context, consequences, and rollback/reversal notes.
- [ ] Remove templates whose fields duplicate the same scope/validation/stop-condition data.
- [ ] Remove prompts that exist primarily to restate those templates rather than provide reusable execution value.

### Task 4: Retire legacy process docs and examples

**Files:**
- Remove superseded numbered workflow docs after their useful content has been consolidated.
- Remove examples that encode mandatory fake-first, Tool Mode, context-level, per-block audit, or per-block handoff behavior.
- Keep examples only when they demonstrate a current V2 gate or safety pattern without introducing mandatory ceremony.

**Interfaces:**
- Consumes: completed consolidated docs from Tasks 1-3.
- Produces: a repository whose visible structure teaches the V2 method instead of preserving contradictory legacy instructions.

- [ ] Delete superseded docs only after confirming their non-redundant rules were preserved.
- [ ] Delete obsolete tooling/bootstrap examples that are no longer part of the canonical workflow.
- [ ] Keep a minimal set of examples for change brief, safety-sensitive work, ADR, and handoff if useful.
- [ ] Search the repository for old canonical phrases such as `Plan -> Block -> Prompt`, `Tool Mode`, `tiny`, `standard`, `full`, and unconditional `fake provider` requirements; remove or qualify remaining references.

### Task 5: Make validation enforce principles instead of historical structure

**Files:**
- Modify: `scripts/validate_playbook_structure.py`
- Review: `scripts/check_repo_contamination.py`
- Modify if needed: `.github/workflows/playbook-validate.yml`

**Interfaces:**
- Consumes: new essential file set.
- Produces: CI that fails on missing V2 essentials or contamination, not on deleted legacy material.

- [ ] Replace the historical required-file list with the small V2 essential set.
- [ ] Add validation for required canonical phrases/links where useful without forcing document length or template proliferation.
- [ ] Preserve contamination checks and least-privilege CI.
- [ ] Ensure the GitHub Actions workflow still runs both structure and contamination validation.

### Task 6: Verify and review the migration

**Files:**
- All files changed by Tasks 1-5.

**Interfaces:**
- Consumes: complete V2 branch.
- Produces: reviewable branch ready for PR, with no contradictions between current and legacy guidance.

- [ ] Run the repository structure validator.
- [ ] Run the contamination checker.
- [ ] Compare the branch against `main` and inspect every changed path.
- [ ] Search for contradictory legacy workflow language and remove remaining active references.
- [ ] Confirm that low-risk work can be described without a spec, Tool Mode, audit summary, or handoff while risky work still activates explicit safety/design/audit controls.
- [ ] Open a draft PR summarizing removed ceremony, retained safety guarantees, and residual migration risks.
