# Skill Intake Runbook

## Objective

Import a new skill into the registry safely and decide whether it should be promoted to active use.

## Steps

1. Identify the missing capability.
2. Confirm the skill is not already in the active registry.
3. Import the candidate skill into the quarantine path.
4. Validate metadata and file structure.
5. Review scripts, references, and assets for risk.
6. Run a representative evaluation task.
7. Record provenance and evaluation outcome.
8. Approve and promote, or reject and archive.

## Validation Checklist

- `SKILL.md` exists
- frontmatter has `name` and `description`
- scripts resolve and are reviewable
- references are linked from `SKILL.md`
- no destructive default behavior
- no embedded secrets
- evaluation result attached

## Promotion Criteria

- capability gap is real
- skill quality is acceptable
- source is trusted or explicitly approved
- evaluation passed
- provenance record completed
