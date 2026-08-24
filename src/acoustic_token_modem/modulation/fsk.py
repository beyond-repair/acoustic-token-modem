"""Binary FSK modulator / demodulator (simulation baseline)."""

from __future__ import annotations

from typing import List, Sequence, Tuple

import numpy as np


def modulate_fsk(
    bits: Sequence[int],
    *,
    sample_rate: float = 48000.0,
    f0: float = 2000.0,
    f1: float = 4000.0,
    symbol_samples: int = 240,
    amplitude: float = 0.5,
) -> np.ndarray:
    """Map bits to concatenated FSK tones. Returns float64 waveform in [-1, 1]."""
    if symbol_samples < 8:
        raise ValueError("symbol_samples too small")
    t = np.arange(symbol_samples) / sample_rate
    tone0 = amplitude * np.sin(2 * np.pi * f0 * t)
    tone1 = amplitude * np.sin(2 * np.pi * f1 * t)
    chunks = []
    for b in bits:
        chunks.append(tone1 if int(b) & 1 else tone0)
    if not chunks:
        return np.zeros(0, dtype=np.float64)
    return np.concatenate(chunks).astype(np.float64)


def demodulate_fsk(
    waveform: np.ndarray,
    n_bits: int,
    *,
    sample_rate: float = 48000.0,
    f0: float = 2000.0,
    f1: float = 4000.0,
    symbol_samples: int = 240,
) -> List[int]:
    """Non-coherent energy comparison per symbol (simple baseline)."""
    bits: List[int] = []
    for i in range(n_bits):
        start = i * symbol_samples
        end = start + symbol_samples
        if end > len(waveform):
            raise ValueError("waveform shorter than expected bit count")
        seg = waveform[start:end]
        t = np.arange(symbol_samples) / sample_rate
        # Correlate against pure tones
        c0 = np.sum(seg * np.sin(2 * np.pi * f0 * t))
        c1 = np.sum(seg * np.sin(2 * np.pi * f1 * t))
        bits.append(1 if abs(c1) >= abs(c0) else 0)
    return bits
