# Playbook V2.1 Refinement Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Refine the risk-based V2 workflow so agents do the workflow without narrating it, while reducing six named gates to four true escalations plus Isolation and Handoff supporting rules.

**Architecture:** `docs/workflow.md` remains canonical. README and durable invariants mirror only the essential concepts. Safety distinguishes implementation/testing from destructive execution against real state; testing owns Isolation; handoff is continuity support rather than a workflow gate.

**Tech Stack:** Markdown documentation, Python structure validator, GitHub Actions.

## Global Constraints

- Preserve `Inspect -> Implement -> Verify -> Review` as the universal loop.
- Do not require process narration, gate-status output, risk tiers, Tool Mode, or context levels.
- Keep Plan, Design, Safety, and Audit as the only escalations.
- Treat Isolation as a verification/testing rule and Handoff as a continuity trigger.
- Confirmation is required for dangerous execution against real state, not for implementing or testing the capability safely.
- Diff size alone must not trigger formal audit.
- Preserve all repository/data/security guardrails and mandatory verification.

---

### Task 1: Refine canonical workflow

**Files:** `docs/workflow.md`, `README.md`

- [ ] Add an anti-ceremony rule: do the workflow; do not narrate process metadata unless useful.
- [ ] Reduce Triggered Gates to Plan, Design, Safety, Audit.
- [ ] Move fake guidance to an Isolation Rule and handoff guidance to a Handoff Trigger.
- [ ] Make Plan activation depend on whether planning can materially change implementation, placement, or order.
- [ ] Make Design about durable strategy/decision rather than any public API edit.
- [ ] Make Audit impact-based; diff size alone is insufficient.
- [ ] Clarify that smallest coherent change means smallest complete solution, not smallest possible diff.

### Task 2: Align safety, testing, architecture, invariants, and templates

**Files:** `docs/safety.md`, `docs/testing.md`, `docs/architecture.md`, `AGENTS.md`, `templates/handoff.md`, `examples/app-shell/app-feature-spec-example.md`, `examples/forge-core/block-example.md`

- [ ] Separate safe implementation/testing from applying destructive actions to real state.
- [ ] Rename/remove Fake Gate references in favor of Isolation Rule.
- [ ] Rename/remove Handoff Gate references in favor of Handoff Trigger.
- [ ] Clarify API edits versus API strategy in Design guidance.
- [ ] Keep the normal-change example free of process narration.
- [ ] Keep one external-boundary example demonstrating Isolation without mandatory abstraction.

### Task 3: Align validator and PR description

**Files:** `scripts/validate_playbook_structure.py`, PR #2 body

- [ ] Update canonical phrase checks if they encode the old six-gate model.
- [ ] Ensure validator still rejects legacy process directories/docs.
- [ ] Update PR summary from six gates to four escalations + two supporting rules.
- [ ] Remove this temporary plan after implementation.

### Task 4: Verify

- [ ] Inspect branch diff against the pre-V2.1 head.
- [ ] Run GitHub Actions `Playbook Validate` on final head.
- [ ] Confirm no active V2 file treats Fake or Handoff as a gate.
- [ ] Confirm real-state destructive execution still requires explicit apply intent/confirmation where appropriate.
