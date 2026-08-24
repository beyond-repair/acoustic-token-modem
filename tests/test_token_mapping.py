from acoustic_token_modem.tokenizer.token_mapper import TokenMapper
from acoustic_token_modem.tokenizer.vocabulary import TokenVocabulary


def test_bits_per_token():
    v = TokenVocabulary(size=50257)  # GPT-2-like size as example only
    assert v.bits_per_token == 16


def test_roundtrip_ids():
    v = TokenVocabulary(size=256)
    m = TokenMapper(v)
    ids = [0, 1, 127, 255, 42]
    raw = m.encode(ids)
    assert m.decode(raw, len(ids)) == ids


def test_out_of_range():
    v = TokenVocabulary(size=10)
    m = TokenMapper(v)
    try:
        m.encode([10])
        assert False
    except ValueError:
        pass
