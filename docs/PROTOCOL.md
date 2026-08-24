# Protocol (draft v0)

Status: **draft**. Not frozen until M12.

## Goals

- Deterministic serialization  
- Explicit versioning  
- Sequence numbers  
- Integrity (CRC)  
- Fragmentation / reassembly  
- Loss and duplicate detection  

## Packet fields (logical)

| Field | Purpose |
|-------|---------|
| MAGIC | Fixed sync word |
| VERSION | Protocol version |
| MODE | Modulation / coding hint |
| SESSION_ID | Session demux |
| SEQUENCE_ID | Ordering / loss detection |
| TOKEN_COUNT | Number of token IDs in payload |
| PAYLOAD_LENGTH | Byte length of payload |
| PAYLOAD | Packed token bits (or compressed) |
| FEC | Forward error correction parity |
| CRC | Integrity over header+payload (+FEC policy TBD) |

Exact binary layout: `docs/PACKET_FORMAT.md`.

## Reconstruction rule

Receiver must emit the **exact** original token ID sequence or signal hard failure. Silent partial recovery is not success for the research invariant.
