# Claim status — acoustic-token-modem

**Classification:** RESEARCH  
**Claim level:** 1 (software/simulation evidence only)  
**Governing source:** [ADL-Governance](https://github.com/beyond-repair/ADL-Governance)

## Allowed

- Token ID → packet → FSK *simulation* → reconstruct tokens (unit tests).
- Document protocol, packet format, and metrics *definitions*.
- State that CI (`pytest.yml`) exercises the simulation suite.

## Forbidden without new measurement (UNSUPPORTED)

- Reporting theoretical bitrate as achieved bitrate. **UNSUPPORTED**
- Claiming real speaker/mic performance (M10 not implemented). **UNSUPPORTED**
- Claiming novelty of the physical layer from “AI tokens” alone. **UNSUPPORTED**
- Promoting claim level above 1 based on GitHub Actions success. **UNSUPPORTED**
- Treating PSK/QAM/OFDM stubs as working modulators. **UNSUPPORTED**

## Evidence bound

| Item | Status |
|------|--------|
| Local/CI pytest | Sweep-092 run **34068585607** conclusion **success** (sim); Sweep-066 run **33995308862** success |
| Hardware M10 | Not present |
| Prior-art table | Template only (`docs/RESEARCH.md`) |
| Benchmarks/results | Empty placeholder |

Sweep-110 does not raise claim level.
