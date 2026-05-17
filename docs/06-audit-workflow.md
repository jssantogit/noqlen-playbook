# Audit Workflow

Audit types:

- Implementation audit.
- Architecture audit.
- Security audit.
- Repo hygiene audit.
- App boundary audit.
- Release audit.

Audit is mandatory:

- After large blocks.
- After risky blocks.
- After public API changes.
- After app/core boundary changes.
- After file operation changes.
- Before release.

Audits compare the diff against the spec, verify validation evidence, check boundary discipline, identify security and hygiene risks, and classify findings as required fixes or optional improvements.

Audits must state whether compressed, sandboxed, or tool-assisted outputs were used. High-risk audits need raw evidence for failures, not only compressed summaries.

Semantic tool edits must be checked against the declared scope, allowed files, forbidden files, and active spec.

Tool metrics, summarized output, or compressed output can support an audit, but they do not prove correctness. The audit still checks spec fit, boundaries, risk, validation evidence, repo hygiene, and whether raw evidence is available where needed.
