"""Map token ID sequences to packed bits and back."""

from __future__ import annotations

from typing import List, Sequence

from acoustic_token_modem.tokenizer.vocabulary import TokenVocabulary


class TokenMapper:
    """Fixed-width packing of integer token IDs (M1). Entropy coding is Phase 3."""

    def __init__(self, vocabulary: TokenVocabulary):
        self.vocabulary = vocabulary
        self.width = vocabulary.bits_per_token

    def encode(self, token_ids: Sequence[int]) -> bytes:
        for t in token_ids:
            self.vocabulary.validate_id(int(t))
        if not token_ids:
            return b""
        # Bit pack MSB-first within each token, stream MSB-first
        bits: List[int] = []
        for t in token_ids:
            v = int(t)
            for i in range(self.width - 1, -1, -1):
                bits.append((v >> i) & 1)
        # Pad to byte boundary with zeros
        while len(bits) % 8 != 0:
            bits.append(0)
        out = bytearray()
        for i in range(0, len(bits), 8):
            byte = 0
            for b in bits[i : i + 8]:
                byte = (byte << 1) | b
            out.append(byte)
        return bytes(out)

    def decode(self, data: bytes, token_count: int) -> List[int]:
        if token_count < 0:
            raise ValueError("token_count must be >= 0")
        if token_count == 0:
            return []
        need_bits = token_count * self.width
        bits: List[int] = []
        for byte in data:
            for i in range(7, -1, -1):
                bits.append((byte >> i) & 1)
                if len(bits) >= need_bits:
                    break
            if len(bits) >= need_bits:
                break
        if len(bits) < need_bits:
            raise ValueError("insufficient bits for token_count")
        tokens: List[int] = []
        for i in range(token_count):
            v = 0
            base = i * self.width
            for j in range(self.width):
                v = (v << 1) | bits[base + j]
            self.vocabulary.validate_id(v)
            tokens.append(v)
        return tokens
