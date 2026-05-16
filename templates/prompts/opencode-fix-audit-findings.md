# Opencode Prompt: Fix Audit Findings

Purpose: Fix only audit findings.

## Prompt

Findings list: `<findings>`

Allowed files: `<allowed files>`

Forbidden files: `<forbidden files>`

Validation: `<commands>`

Requirements:

- Fix only listed required findings.
- Do not broaden scope.
- Preserve unrelated files.
- Stop after fixes and validation.

Output: touched files, fixed findings, validation summary, and remaining risks.
