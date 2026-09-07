# Governance — acoustic-token-modem

**Classification:** RESEARCH  
**Governing source:** [ADL-Governance](https://github.com/beyond-repair/ADL-Governance)  
**Sweep:** 110 (2026-09-07)

## Invariants

1. Simulation evidence does not equal hardware validation.
2. Claim level remains **1** until speaker/mic measurements exist (M10).
3. Theoretical bitrate SHALL NOT be reported as achieved bitrate.
4. Novelty of an "AI token physical layer" is **UNSUPPORTED** without prior-art measurement.
5. Green pytest CI SHALL NOT raise claim level.

## Allowed product surface

- Token → packet → FSK simulation → reconstruct tokens.
- Protocol and metric *definitions*.
- Empty benchmark placeholder until measured results are committed.

## Forbidden without operator + measurement

- M10 live speaker/mic claims.
- OFDM/PSK/QAM performance claims (stubs only).
- Productization / ACTIVE promotion.
