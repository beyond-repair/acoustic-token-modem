"""Packet error rate helper."""

from __future__ import annotations


def packet_error_rate(n_fail: int, n_total: int) -> float:
    if n_total <= 0:
        raise ValueError("n_total must be > 0")
    return n_fail / n_total
