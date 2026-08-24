"""AWGN helper."""

from __future__ import annotations

import numpy as np


def add_awgn(signal: np.ndarray, snr_db: float, rng: np.random.Generator | None = None) -> np.ndarray:
    """Add white Gaussian noise for a target SNR (dB) relative to signal power."""
    if signal.size == 0:
        return signal.copy()
    rng = rng or np.random.default_rng(0)
    power = float(np.mean(np.square(signal)))
    if power <= 0:
        return signal.copy()
    snr_lin = 10 ** (snr_db / 10.0)
    noise_power = power / snr_lin
    noise = rng.normal(0.0, np.sqrt(noise_power), size=signal.shape)
    return (signal + noise).astype(np.float64)
