# Agent Tooling Pilot Example

## Block

Evaluate `serena-ro` for a low-risk documentation block.

## Tool Mode

`serena-ro`

## Allowed Use

- Inspect headings and references.
- Locate related docs without reading every file in full.
- Summarize candidate files for the block.

## Forbidden Use

- Edit files through semantic tooling.
- Create local agent configs or tool state.
- Replace validation or audit.
- Read or copy private local data.

## Validation

- Run `python3 scripts/validate_playbook_structure.py`.
- Run `python3 scripts/check_repo_contamination.py`.
- Audit touched files against the block scope.

## Pilot Result Format

- Context level used: `<tiny | standard | full>`.
- Tool mode used: `serena-ro`.
- Commands compressed: `<none or list>`.
- Raw failure evidence available: `<yes | no | not applicable>`.
- Re-runs caused by missing details: `<count>`.
- Audit findings caused by insufficient context: `<count>`.
- Recommendation: `<continue optional pilot | stop pilot | promote to recommended optional use>`.
