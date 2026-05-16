# Workflow Retrofit Patterns

Retrofitting an existing Noqlen repository means adding the current workflow around the project without refactoring the product during the workflow block.

## Phase 1: Inventory

- Identify purpose, public entry points, core packages, docs, tests, CI, release files, local tooling, and generated artifacts.
- Record existing safety, dry-run, fake, fixture, handoff, and audit material.
- Do not change behavior during inventory.

## Phase 2: Add Context Files

- Add compact current context.
- Add a handoff or delta summary if the repository lacks one.
- Define allowed files, forbidden files, validation commands, active block, non-goals, and stop condition.

## Phase 3: Add Specs For Active Work

- Add specs only for active or upcoming non-trivial work.
- Include requirements, design, tasks, and review evidence.
- Do not backfill large historical specs unless they support an active decision.

## Phase 4: Add ADRs Only Where Needed

- Use ADRs for architecture decisions, hard-to-reverse boundaries, dependencies, storage strategy, public API strategy, app/core strategy, or security policy.
- Do not write ADRs for simple implementation details.

## Phase 5: Add Validation And Audit Checklists

- Define validation proportional to risk.
- Add audit checks for scope, specs, tests, security, repo hygiene, boundaries, and release readiness.
- Require touched files and validation evidence in each block summary.

## Phase 6: Add Fake-First And Dry-Run-First Examples

- Document fake providers, fake clients, synthetic fixtures, and temporary workspaces.
- Make dry-run the default for file operations, provider execution, service lifecycle, imports, cleanup, and publishing.
- Never require real network, real service, or real music library access for automated tests.

## Phase 7: Add Release And Repo Hygiene Checks

- Add repository hygiene checks for secrets, personal paths, generated artifacts, local tooling, and deployment output.
- Add release readiness docs before tagging or publishing.
- Use GitHub Actions for deploy or release automation when applicable.

## Phase 8: Update Handoff

- Summarize completed blocks, validation, decisions, risks, pending work, and next recommended block.
- Link the public API surface or consumer boundary that the next repository should use.

## Workflow-Ready Criteria

- Current context exists and is accurate.
- Active work has a spec or explicit reason it does not need one.
- Architectural decisions are recorded only where useful.
- Validation commands are known and have recent evidence.
- Audit checklist exists for meaningful changes.
- Fake-first and dry-run-first behavior is documented for risky integrations.
- Repo hygiene checks pass.
- Handoff explains the next safe block.

## Avoid During Retrofit

- Broad product refactors.
- Rewriting working docs for style only.
- Adding dependencies for workflow metadata.
- Running risky tests, real services, or real libraries.
- Copying private configs, local paths, secrets, lyrics, fingerprints, or private data into docs.
- Treating retrofit as a release, app implementation, or architecture redesign.
