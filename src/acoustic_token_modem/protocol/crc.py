"""CRC32 (IEEE) for packet integrity."""

from __future__ import annotations

import zlib


def crc32(data: bytes) -> int:
    return zlib.crc32(data) & 0xFFFFFFFF


def crc32_bytes(data: bytes) -> bytes:
    return crc32(data).to_bytes(4, "big")
