from app.protocols import choose_interop_protocol


def test_choose_interop_protocol_prefers_a2a_by_default():
    assert choose_interop_protocol('remote specialist delegation') == 'a2a'


def test_choose_interop_protocol_selects_acp_for_legacy_beeai_cases():
    assert choose_interop_protocol('legacy ACP integration with BeeAI agent') == 'acp'


def test_choose_interop_protocol_selects_anp_for_decentralized_networking():
    assert choose_interop_protocol('decentralized marketplace discovery') == 'anp'
