# Future Agent Boundary Example

## Allowed files

- Files listed in the active block.

## Forbidden files

- Secrets, release configuration, unrelated modules, generated artifacts, and local tooling directories.

## Capabilities

- Read context.
- Edit allowed files.
- Run validation commands.
- Report touched files and risks.

## Stop condition

Stop if forbidden files are needed, requirements are unclear, validation changes scope, or destructive actions would be required.

## Validation

Run the commands listed in the block and report pass/fail evidence.
