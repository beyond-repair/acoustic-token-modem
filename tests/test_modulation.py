import numpy as np

from acoustic_token_modem.modulation.fsk import demodulate_fsk, modulate_fsk


def test_fsk_clean_channel():
    bits = [0, 1, 1, 0, 1, 0, 0, 1] * 4
    wave = modulate_fsk(bits, sample_rate=48000, symbol_samples=240)
    rx = demodulate_fsk(wave, len(bits), sample_rate=48000, symbol_samples=240)
    assert rx == bits
