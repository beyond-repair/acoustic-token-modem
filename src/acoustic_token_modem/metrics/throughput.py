"""Throughput helpers."""

from __future__ import annotations


def token_density(n_tokens_ok: int, elapsed_seconds: float) -> float:
    if elapsed_seconds <= 0:
        raise ValueError("elapsed_seconds must be > 0")
    return n_tokens_ok / elapsed_seconds


def effective_payload_bps(payload_bits_ok: int, elapsed_seconds: float) -> float:
    if elapsed_seconds <= 0:
        raise ValueError("elapsed_seconds must be > 0")
    return payload_bits_ok / elapsed_seconds
