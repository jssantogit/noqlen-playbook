# Opencode Prompt: Retrofit Existing Repository

Purpose: Guide an agent to apply the playbook to an existing repository safely.

## Prompt

Task: retrofit current Noqlen workflow scaffolding into an existing repository.

Requirements:

- Inspect first.
- Add context files.
- Add spec templates or an active spec for current work.
- Add an ADR only if needed for an architectural decision.
- Add validation checklist.
- Add audit checklist.
- Keep changes commit-sized.
- Do not perform broad rewrites.
- Do not refactor product code during workflow retrofit.
- Do not add dependencies unless explicitly approved.

Output:

- Files touched.
- Validation run.
- Workflow-ready gaps remaining.
- Recommended next block.

Stop condition: stop if product behavior changes become necessary or forbidden files are needed.
