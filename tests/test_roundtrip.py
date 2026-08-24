"""Central invariant: tokens_in == tokens_out under clean FSK simulation."""

from acoustic_token_modem.coding.symbol_mapper import bits_to_bytes, bytes_to_bits
from acoustic_token_modem.modulation.fsk import demodulate_fsk, modulate_fsk
from acoustic_token_modem.protocol.framing import packet_to_tokens, tokens_to_packet
from acoustic_token_modem.protocol.packet import Packet
from acoustic_token_modem.tokenizer.vocabulary import TokenVocabulary


def test_tokens_fsk_tokens_clean():
    v = TokenVocabulary(size=4096)
    tokens_in = [1820, 391, 772 % 4096, 42, 100, 2000]
    pkt = tokens_to_packet(tokens_in, v, session_id=1, sequence_id=0)
    frame = pkt.serialize()
    bits = bytes_to_bits(frame)
    wave = modulate_fsk(bits, sample_rate=48000, symbol_samples=120)
    bits_rx = demodulate_fsk(wave, len(bits), sample_rate=48000, symbol_samples=120)
    frame_rx = bits_to_bytes(bits_rx)
    pkt_rx = Packet.deserialize(frame_rx)
    tokens_out = packet_to_tokens(pkt_rx, v)
    assert tokens_out == tokens_in
