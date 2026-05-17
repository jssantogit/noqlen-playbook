# Opencode Prompt: Evaluate Agent Tooling

Purpose: Evaluate optional agent tooling for one low-risk block without installing tools or committing local configs.

## Prompt

Task: evaluate whether `<tool or mode>` would help `<block type>`.

Tool Mode: `<none | native | serena-ro | serena-edit | rtk | context-mode | caveman-limited | combo>`

Scope: `<scope>`

Allowed files: `<allowed files>`

Forbidden files: `<forbidden files, active local agent configs, generated tool state>`

Tool permissions: `<read-only | edit allowed files only | summarize output only>`

Raw evidence requirements: `<what raw output must be preserved>`

Compression limits: do not hide failures, assumptions, validation commands, touched files, risks, or stop conditions.

Validation: `<commands>`

Output: recommendation, benefits, risks, validation evidence, raw evidence status, and whether the tool should remain optional.

Stop condition: stop if installation, local config creation, forbidden files, destructive actions, or broader scope would be required.
