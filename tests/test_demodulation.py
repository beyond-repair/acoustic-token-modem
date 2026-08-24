from acoustic_token_modem.demodulation.detector import rms
import numpy as np


def test_rms():
    x = np.ones(10)
    assert abs(rms(x) - 1.0) < 1e-9
