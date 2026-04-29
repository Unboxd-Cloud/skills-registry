"""Local skill registry control-plane helpers for a self-improving agent."""

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class SkillSearchResult:
    name: str
    path: str
    source: str
    state: str


@dataclass(frozen=True)
class CapabilityGap:
    capability: str
    reason: str


class SkillRegistry:
    def __init__(self, active_path: str, quarantine_path: str, authoring_path: str):
        self.active_path = Path(active_path).expanduser()
        self.quarantine_path = Path(quarantine_path).expanduser()
        self.authoring_path = Path(authoring_path).expanduser()

    def search(self, query: str) -> list[SkillSearchResult]:
        roots = [
            (self.active_path, 'local-active', 'active'),
            (self.quarantine_path, 'local-quarantine', 'quarantine'),
            (self.authoring_path, 'local-authoring', 'authoring'),
        ]
        results: list[SkillSearchResult] = []
        lowered = query.lower()
        for root, source, state in roots:
            if not root.exists():
                continue
            for skill_file in root.glob('*/SKILL.md'):
                name = skill_file.parent.name
                if lowered in name.lower() or lowered in skill_file.read_text().lower():
                    results.append(SkillSearchResult(name=name, path=str(skill_file.parent), source=source, state=state))
        return results

    def detect_capability_gap(self, requested_capability: str, discovered_skills: Iterable[SkillSearchResult]) -> CapabilityGap | None:
        for skill in discovered_skills:
            if requested_capability.lower() in skill.name.lower():
                return None
        return CapabilityGap(
            capability=requested_capability,
            reason=f'No matching skill found for capability: {requested_capability}',
        )
