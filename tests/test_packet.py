from acoustic_token_modem.protocol.framing import packet_to_tokens, tokens_to_packet
from acoustic_token_modem.protocol.packet import Packet
from acoustic_token_modem.tokenizer.vocabulary import TokenVocabulary


def test_packet_crc_roundtrip():
    p = Packet(session_id=7, sequence_id=3, token_count=0, payload=b"\x00\x01")
    raw = p.serialize()
    q = Packet.deserialize(raw)
    assert q.session_id == 7
    assert q.sequence_id == 3
    assert q.payload == b"\x00\x01"


def test_tokens_packet_tokens():
    v = TokenVocabulary(size=1000)
    ids = [1820 % 1000, 391, 42, 7]
    pkt = tokens_to_packet(ids, v, session_id=1, sequence_id=9)
    raw = pkt.serialize()
    pkt2 = Packet.deserialize(raw)
    assert packet_to_tokens(pkt2, v) == ids
