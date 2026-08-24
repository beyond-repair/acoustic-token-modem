# Security model

This is a **communications protocol**, not an authentication product by default.

## Accidental vs intentional corruption

| Mechanism | Purpose |
|-----------|---------|
| CRC | Accidental bit errors |
| Sequence / session | Loss, reorder, simple replay surface |
| Optional crypto auth (future) | Tampering, impersonation |

## Threats to document as the stack matures

Packet auth · replay · malformed packets · resource exhaustion · acoustic injection · token-stream tampering

Reject packets that fail CRC or sequence windows. Do not execute payload as code.
