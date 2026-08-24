"""Binary packet serialize / deserialize (v0)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from acoustic_token_modem.protocol.crc import crc32, crc32_bytes

MAGIC = 0x41544D30  # ATM0
VERSION = 0


@dataclass(frozen=True)
class Packet:
    session_id: int
    sequence_id: int
    token_count: int
    payload: bytes
    mode: int = 0
    fec: bytes = b""

    def serialize(self) -> bytes:
        if not (0 <= self.session_id <= 0xFFFF):
            raise ValueError("session_id out of range")
        if not (0 <= self.sequence_id <= 0xFFFFFFFF):
            raise ValueError("sequence_id out of range")
        if not (0 <= self.token_count <= 0xFFFF):
            raise ValueError("token_count out of range")
        if len(self.payload) > 0xFFFF:
            raise ValueError("payload too long")
        header = (
            MAGIC.to_bytes(4, "big")
            + bytes([VERSION, self.mode & 0xFF])
            + self.session_id.to_bytes(2, "big")
            + self.sequence_id.to_bytes(4, "big")
            + self.token_count.to_bytes(2, "big")
            + len(self.payload).to_bytes(2, "big")
        )
        body = header + self.payload + self.fec
        return body + crc32_bytes(body)

    @classmethod
    def deserialize(cls, data: bytes, fec_length: int = 0) -> "Packet":
        if len(data) < 20:
            raise ValueError("packet too short")
        if int.from_bytes(data[0:4], "big") != MAGIC:
            raise ValueError("bad MAGIC")
        version = data[4]
        if version != VERSION:
            raise ValueError(f"unsupported VERSION {version}")
        mode = data[5]
        session_id = int.from_bytes(data[6:8], "big")
        sequence_id = int.from_bytes(data[8:12], "big")
        token_count = int.from_bytes(data[12:14], "big")
        payload_length = int.from_bytes(data[14:16], "big")
        need = 16 + payload_length + fec_length + 4
        if len(data) < need:
            raise ValueError("truncated packet")
        payload = data[16 : 16 + payload_length]
        fec = data[16 + payload_length : 16 + payload_length + fec_length]
        body = data[: 16 + payload_length + fec_length]
        got_crc = int.from_bytes(data[16 + payload_length + fec_length : need], "big")
        if crc32(body) != got_crc:
            raise ValueError("CRC mismatch")
        return cls(
            session_id=session_id,
            sequence_id=sequence_id,
            token_count=token_count,
            payload=payload,
            mode=mode,
            fec=fec,
        )
