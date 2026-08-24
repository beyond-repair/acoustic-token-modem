#!/usr/bin/env python3
"""M3 baseline: FSK token roundtrip under AWGN sweep (simulation only)."""

from __future__ import annotations

import json
from pathlib import Path

from acoustic_token_modem.channel.simulation import ChannelConfig, simulate_channel
from acoustic_token_modem.coding.symbol_mapper import bits_to_bytes, bytes_to_bits
from acoustic_token_modem.metrics.ber import bit_error_rate
from acoustic_token_modem.modulation.fsk import demodulate_fsk, modulate_fsk
from acoustic_token_modem.protocol.framing import packet_to_tokens, tokens_to_packet
from acoustic_token_modem.protocol.packet import Packet
from acoustic_token_modem.tokenizer.vocabulary import TokenVocabulary


def run_once(snr_db: float, seed: int = 0) -> dict:
    v = TokenVocabulary(size=4096)
    tokens_in = [i % 4096 for i in range(32)]
    pkt = tokens_to_packet(tokens_in, v, session_id=1, sequence_id=0)
    frame = pkt.serialize()
    bits = bytes_to_bits(frame)
    wave = modulate_fsk(bits, symbol_samples=120)
    noisy = simulate_channel(wave, ChannelConfig(snr_db=snr_db, seed=seed))
    try:
        bits_rx = demodulate_fsk(noisy, len(bits), symbol_samples=120)
        ber = bit_error_rate(bits, bits_rx)
        frame_rx = bits_to_bytes(bits_rx)
        pkt_rx = Packet.deserialize(frame_rx)
        tokens_out = packet_to_tokens(pkt_rx, v)
        ok = tokens_out == tokens_in
    except Exception as e:
        return {"snr_db": snr_db, "ok": False, "error": str(e), "ber": None}
    return {"snr_db": snr_db, "ok": ok, "ber": ber, "error": None}


def main() -> None:
    results = [run_once(snr) for snr in [0, 5, 10, 15, 20, 30]]
    out = Path(__file__).resolve().parents[1] / "benchmarks" / "results" / "baseline_fsk_awgn.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
