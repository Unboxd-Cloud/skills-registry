"""Protocol selection helpers for multi-protocol agent interoperability."""


def choose_interop_protocol(use_case: str) -> str:
    lowered = use_case.lower()
    if 'decentralized' in lowered or 'marketplace' in lowered:
        return 'anp'
    if 'beeai' in lowered or 'legacy acp' in lowered or 'acp' in lowered:
        return 'acp'
    return 'a2a'
