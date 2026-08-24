"""Detection helpers (energy / threshold)."""

from __future__ import annotations

import numpy as np


def rms(x: np.ndarray) -> float:
    if x.size == 0:
        return 0.0
    return float(np.sqrt(np.mean(np.square(x))))
