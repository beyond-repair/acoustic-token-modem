"""Bit error rate."""

from __future__ import annotations

from typing import Sequence


def bit_error_rate(tx: Sequence[int], rx: Sequence[int]) -> float:
    if len(tx) != len(rx):
        raise ValueError("length mismatch")
    if not tx:
        return 0.0
    err = sum(int(a) != int(b) for a, b in zip(tx, rx))
    return err / len(tx)
