"""High-level frame: tokens ↔ packet bytes."""

from __future__ import annotations

from typing import List, Sequence

from acoustic_token_modem.protocol.packet import Packet
from acoustic_token_modem.tokenizer.token_mapper import TokenMapper
from acoustic_token_modem.tokenizer.vocabulary import TokenVocabulary


def tokens_to_packet(
    token_ids: Sequence[int],
    vocabulary: TokenVocabulary,
    *,
    session_id: int = 1,
    sequence_id: int = 0,
    mode: int = 0,
) -> Packet:
    mapper = TokenMapper(vocabulary)
    payload = mapper.encode(token_ids)
    return Packet(
        session_id=session_id,
        sequence_id=sequence_id,
        token_count=len(token_ids),
        payload=payload,
        mode=mode,
    )


def packet_to_tokens(packet: Packet, vocabulary: TokenVocabulary) -> List[int]:
    mapper = TokenMapper(vocabulary)
    return mapper.decode(packet.payload, packet.token_count)
