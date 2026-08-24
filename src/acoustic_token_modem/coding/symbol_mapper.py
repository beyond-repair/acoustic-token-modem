"""Map bytes to binary symbols (0/1) for FSK baseline."""

from __future__ import annotations

from typing import List


def bytes_to_bits(data: bytes) -> List[int]:
    bits: List[int] = []
    for byte in data:
        for i in range(7, -1, -1):
            bits.append((byte >> i) & 1)
    return bits


def bits_to_bytes(bits: List[int]) -> bytes:
    if len(bits) % 8 != 0:
        raise ValueError("bit length must be multiple of 8")
    out = bytearray()
    for i in range(0, len(bits), 8):
        byte = 0
        for b in bits[i : i + 8]:
            byte = (byte << 1) | (b & 1)
        out.append(byte)
    return bytes(out)
