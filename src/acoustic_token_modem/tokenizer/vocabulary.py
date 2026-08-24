"""Tokenizer-independent vocabulary abstraction."""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class TokenVocabulary:
    """
    Abstract vocabulary size for bit-width calculation.
    Does not assume any particular LLM tokenizer.
    """

    size: int
    name: str = "generic"

    def __post_init__(self) -> None:
        if self.size < 2:
            raise ValueError("vocabulary size must be >= 2")

    @property
    def bits_per_token(self) -> int:
        return math.ceil(math.log2(self.size))

    def validate_id(self, token_id: int) -> None:
        if not (0 <= token_id < self.size):
            raise ValueError(f"token_id {token_id} out of range [0, {self.size})")
