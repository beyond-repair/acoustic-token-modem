"""FEC placeholder (Phase 5). Identity code for M0–M4."""

from __future__ import annotations


def encode_identity(payload: bytes) -> bytes:
    """No redundancy — baseline before real FEC."""
    return payload


def decode_identity(payload: bytes) -> bytes:
    return payload
