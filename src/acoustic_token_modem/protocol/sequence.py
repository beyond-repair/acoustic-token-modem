"""Sequence window helpers for loss / duplicate detection (M2+)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Set


@dataclass
class SequenceTracker:
    """Simple receiver window: accept seq if not seen; detect gaps."""

    expected: int = 0
    seen: Set[int] = field(default_factory=set)
    max_window: int = 1024

    def observe(self, sequence_id: int) -> str:
        """Return 'ok' | 'duplicate' | 'gap' | 'future'."""
        if sequence_id in self.seen:
            return "duplicate"
        if sequence_id == self.expected:
            self.seen.add(sequence_id)
            self.expected += 1
            self._trim()
            return "ok"
        if sequence_id < self.expected:
            return "duplicate"
        # future or gap
        self.seen.add(sequence_id)
        self._trim()
        return "gap" if sequence_id > self.expected else "future"

    def _trim(self) -> None:
        if len(self.seen) > self.max_window:
            # drop oldest ids
            ordered = sorted(self.seen)
            for x in ordered[: len(ordered) - self.max_window]:
                self.seen.discard(x)
