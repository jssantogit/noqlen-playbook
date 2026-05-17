# Tool Mode Matrix

| Tool Mode | Primary Use | Allowed | Forbidden | Evidence Requirement |
| --- | --- | --- | --- | --- |
| `none` | Default workflow | Normal scoped block work | Assuming tooling is required | Normal validation and audit |
| `native` | OpenCode native | Explicit permissions and scoped execution | Risky operations without approval | Normal validation and audit |
| `context-mode` | Context control | Reduce unnecessary context | Treat summaries as final audit proof | Raw evidence for failures and high-risk audits |
| `rtk` | Command output compression | Summarize noisy git, test, grep/find, and log output | Hide subtle failures or missing details | Preserve raw relevant failures |
| `serena-ro` | Semantic navigation | Inspect symbols, references, and boundaries | Edit files or override scope | Report files inspected and scope fit |
| `serena-edit` | Semantic editing | Edit only explicit allowed files | Broad refactors or forbidden files | Diff checked against scope and allowed files |
| `caveman-limited` | Temporary concise status | Short working updates | Specs, ADRs, audits, handoffs, release notes, public docs | Final output must be compact but complete |
| `combo` | Multiple accelerators | List each tool and evidence rule | Ambiguous tooling or hidden evidence | Raw evidence where required |

Optional tooling accelerates the workflow only when it keeps the same guardrails: scoped blocks, explicit boundaries, validation, audit, and human review.
