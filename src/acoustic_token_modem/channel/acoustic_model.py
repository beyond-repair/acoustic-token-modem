"""Simple multipath / scalar reverb placeholders."""

from __future__ import annotations

import numpy as np


def apply_multipath(signal: np.ndarray, delays_samples: list[int], gains: list[float]) -> np.ndarray:
    if len(delays_samples) != len(gains):
        raise ValueError("delays and gains length mismatch")
    out = np.zeros_like(signal, dtype=np.float64)
    for d, g in zip(delays_samples, gains):
        if d < 0:
            raise ValueError("delay must be >= 0")
        if d == 0:
            out += g * signal
        else:
            out[d:] += g * signal[:-d]
    return out
