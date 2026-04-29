# Skill Registry And Self-Improvement Notes

Use this reference when the agent must create new skills locally, ingest skills from other registries, or improve itself through controlled skill acquisition.

## Objective

Enable the agent to expand its capabilities without turning skill installation into an ungoverned code execution path.

## Required Capabilities

- Create new local skills from observed gaps.
- Search approved external skill registries.
- Import candidate skills into a quarantine path.
- Validate metadata, instructions, scripts, and dependencies.
- Promote approved skills into the active local registry.
- Record provenance, version, trust level, and evaluation results.

## Recommended Architecture

Use a three-tier registry model.

1. `authoring`: where the agent drafts or updates skills.
2. `quarantine`: where imported or generated skills are inspected and evaluated.
3. `active`: the trusted local skill directory used during normal operation.

Do not install third-party skills directly into the active registry.

## Registry Sources

Support these source classes explicitly.

- `local`: skills authored by the agent or team.
- `git`: approved Git repositories pinned by URL and revision.
- `bundle`: tarball or zip artifacts with manifests.
- `marketplace`: curated remote registries with explicit metadata and trust policy.

Each imported skill should carry:
- source type
- source identifier
- version or commit
- import timestamp
- evaluator result
- approval state

## Intake Workflow

1. Detect a capability gap.
2. Check the active registry first.
3. Search approved remote registries.
4. Import the candidate to quarantine.
5. Run structural validation.
6. Run behavioral evaluation on representative tasks.
7. Approve or reject.
8. Promote approved skill to active.
9. Record provenance and test evidence.

## Validation Gates

Minimum checks before promotion:
- `SKILL.md` exists and metadata is valid.
- linked scripts and references resolve correctly.
- instructions are coherent and not obviously unsafe.
- declared commands and dependencies are known.
- example task evaluation passes.
- no prohibited secrets or destructive defaults are present.

## Self-Improvement Rules

- Prefer creating a new skill only when the gap is repeated or strategically important.
- Prefer importing before re-implementing when a trusted skill already solves the problem.
- Never self-install a skill from an untrusted source without quarantine and review.
- Treat skills that execute code or touch external systems as higher-risk imports.
- Keep all skill changes auditable.

## Output Expectations

When this reference is in play, produce:
- registry topology
- source trust model
- intake and promotion workflow
- provenance record format
- validation and evaluation gates
- rollback or disable procedure for bad skills
