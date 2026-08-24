# Packet format (v0 binary sketch)

Endianness: **big-endian** for multi-byte integers.

```text
Offset  Size  Field
0       4     MAGIC = 0x41544D30  ("ATM0")
4       1     VERSION = 0
5       1     MODE
6       2     SESSION_ID
8       4     SEQUENCE_ID
12      2     TOKEN_COUNT
14      2     PAYLOAD_LENGTH (bytes)
16      N     PAYLOAD
16+N    F     FEC (optional; length derived from MODE)
16+N+F  4     CRC32 (IEEE) over bytes [0 .. 16+N+F)
```

Token packing: fixed-width `ceil(log2(vocab_size))` bits per ID unless a compression mode is selected (Phase 3).

This sketch is **not** a claim of optimality.
