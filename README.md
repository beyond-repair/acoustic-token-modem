<div align="center">

# acoustic-token-modem

### Experimental acoustic modem for **direct machine-token** transmission

[![RESEARCH](https://img.shields.io/badge/status-RESEARCH-3b82f6?style=for-the-badge)](https://github.com/beyond-repair/ADL-Governance)
[![Claim level](https://img.shields.io/badge/claim-≤_1-yellow?style=for-the-badge)](docs/RESEARCH.md)

</div>

---

## What this is

An experimental **acoustic modem** that treats AI **token IDs** as a digital payload—not as speech to be recognized.

```text
Token IDs  →  packet  →  symbols  →  acoustic waveform
                                      ↓
                              acoustic channel
                                      ↓
Token IDs  ←  packet  ←  symbols  ←  demodulation
```

**Central invariant:** `tokens_in == tokens_out` (deterministic reconstruction).

**Primary research question:**  
How efficiently can a shared tokenizer vocabulary be used to transmit machine-readable token sequences through an acoustic channel?

---

## What this is not

| Not | Why |
|-----|-----|
| Speech recognition / TTS | Tokens never become words |
| “AI-to-AI breakthrough” product | Results must be measured first |
| Claim of novelty by default | Prior art must be surveyed (`docs/RESEARCH.md`) |
| Guaranteed real-world bitrate | Simulation first; hardware later |

Theoretical bitrate is **never** reported as achieved bitrate.

---

## Development phases (incremental)

| Milestone | Focus |
|-----------|--------|
| **M0** | Repository scaffold |
| **M1** | Token → binary → token roundtrip |
| **M2** | Packetization + CRC |
| **M3** | FSK acoustic **simulation** |
| **M4** | FSK audio-file roundtrip |
| **M5** | FEC |
| **M6** | PSK / QAM comparison |
| **M7** | OFDM prototype |
| **M8–M9** | Multi-carrier + adaptive |
| **M10** | Real speaker/mic |
| **M11–M12** | Benchmarks + protocol v1 decision |

**Rule:** establish FSK baseline before OFDM. Every optimization is measured against the previous baseline.

---

## Quick start (simulation)

```bash
pip install -e ".[dev]"
pytest tests/ -q
python experiments/baseline_fsk.py
```

Hardware modes (`LIVE_MIC` / `LIVE_SPEAKER`) are stubs until M10.

CI: `.github/workflows/pytest.yml` runs the same `pytest tests/` suite. Green CI is **not** hardware validation and does **not** raise claim level.

---

## Metrics that matter

- **Token density:** successfully reconstructed token IDs / second  
- Effective throughput: recovered payload bits / elapsed time  
- BER, PER, latency, SNR, bandwidth, FEC overhead  

Always state: hardware (or sim), bandwidth, SNR, distance, modulation, FEC, packet size, method.

---

## Governance

- Classification: **RESEARCH** (ADL-Governance)  
- Default claim level: **≤ 1** until measured  
- License: MIT  
- Sweep-066 (2026-09-05): added pytest workflow; local suite 12 passed (simulation only).
- See [docs/RESEARCH.md](docs/RESEARCH.md), [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), [SECURITY.md](docs/SECURITY.md)

---

<div align="center">

[Atomic Dream Labs](https://github.com/beyond-repair) · [ADL-Governance](https://github.com/beyond-repair/ADL-Governance)

</div>
