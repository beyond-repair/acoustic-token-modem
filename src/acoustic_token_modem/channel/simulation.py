"""Composable channel simulation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

import numpy as np

from acoustic_token_modem.channel.acoustic_model import apply_multipath
from acoustic_token_modem.channel.noise import add_awgn


@dataclass
class ChannelConfig:
    snr_db: float = 20.0
    multipath_delays: Optional[List[int]] = None
    multipath_gains: Optional[List[float]] = None
    seed: int = 0


def simulate_channel(signal: np.ndarray, config: ChannelConfig) -> np.ndarray:
    x = signal.astype(np.float64)
    if config.multipath_delays and config.multipath_gains:
        x = apply_multipath(x, config.multipath_delays, config.multipath_gains)
    rng = np.random.default_rng(config.seed)
    return add_awgn(x, config.snr_db, rng=rng)
