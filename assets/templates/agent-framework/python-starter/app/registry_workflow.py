"""Capability-gap detection workflow for self-improving skill operations."""

from app.skill_registry import SkillRegistry


class SkillCapabilityWorkflow:
    def __init__(self, registry: SkillRegistry):
        self.registry = registry

    def run(self, requested_capability: str) -> dict:
        discovered = self.registry.search(requested_capability)
        gap = self.registry.detect_capability_gap(requested_capability, discovered)
        return {
            'requested_capability': requested_capability,
            'matches': [skill.name for skill in discovered],
            'gap_detected': gap is not None,
            'reason': None if gap is None else gap.reason,
            'recommended_next_step': (
                'create-or-import-skill' if gap is not None else 'reuse-existing-skill'
            ),
        }
