# CI Security And Audit Evidence

CI validates structure and hygiene. CI does not prove architecture is correct.

## GitHub Actions Validation

This playbook should run repository checks on pull requests and pushes to `main`:

- `python3 scripts/validate_playbook_structure.py`.
- `python3 scripts/check_repo_contamination.py`.

Use least permissions, usually `contents: read`.

## Dependency Review

Use GitHub Dependency Review on pull requests. It is useful even for a docs-first repo because workflow files, scripts, and future examples may introduce dependencies.

## Secret Scanning

Enable secret scanning in repository settings when available. Secret scanning complements, but does not replace, the contamination script or review.

## Branch Protection And Rulesets

Recommended PR checks:

- Playbook structure validation.
- Contamination check.
- Dependency review.
- Secret scanning enabled in repo settings.

Branch protection or rulesets should require the checks that are active for the repository. Do not add release, deploy, GitHub Pages, or package publishing automation in this block.

## Raw Evidence Policy

Raw evidence is required for serious debugging, validation failures, audits, release readiness, boundary changes, and security-sensitive changes.

Raw evidence can live in local terminal history, untracked local logs, CI job logs, PR comments that avoid secrets, issue attachments that are sanitized, or a secure internal artifact store. Raw logs should not be committed because they can contain secrets, personal paths, provider output, auth details, or excessive tool output.

Tool metrics, RTK summaries, Context Mode stats, and CI pass/fail states can support review. They do not prove correctness.

Human or agent audit still checks spec fit, boundaries, risk, evidence quality, security posture, and whether the implementation matches the requested block.

## Future Options

Artifact attestations may be useful for release pipelines later. Do not implement release attestations until a release block explicitly asks for them.
