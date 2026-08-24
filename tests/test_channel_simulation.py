import numpy as np

from acoustic_token_modem.channel.simulation import ChannelConfig, simulate_channel
from acoustic_token_modem.modulation.fsk import demodulate_fsk, modulate_fsk
from acoustic_token_modem.metrics.ber import bit_error_rate


def test_high_snr_low_ber():
    bits = [0, 1] * 64
    wave = modulate_fsk(bits, symbol_samples=240)
    noisy = simulate_channel(wave, ChannelConfig(snr_db=30.0, seed=1))
    rx = demodulate_fsk(noisy, len(bits), symbol_samples=240)
    assert bit_error_rate(bits, rx) < 0.05
