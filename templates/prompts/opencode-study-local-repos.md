# Opencode Prompt: Study Local Repositories

Purpose: Guide an agent to inspect local repositories read-only and produce sanitized workflow observations.

## Prompt

Task: inspect nearby Noqlen repositories read-only and summarize workflow lessons.

Rules:

- Read-only only.
- Do not modify inspected repositories.
- Do not run tests, builds, formatters, installers, or commands that write artifacts.
- Do not stage or commit files from inspected repositories.
- Do not include absolute local paths.
- Do not copy secrets, private data, personal paths, lyrics, fingerprints, real library paths, or full local configs.

Inspect:

- Top-level structure.
- Docs, context, specs, ADRs, tests, CI, release files, audits, and handoffs.
- CLI/core, service/core, provider/core, or app/core boundaries.
- Fake-first, dry-run-first, validation, and repo hygiene signs.

Output:

- Repositories found.
- Sanitized structure summary.
- Workflow strengths.
- Workflow gaps.
- Risks.
- Suggested playbook examples.
