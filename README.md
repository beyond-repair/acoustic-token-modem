<div align="center">

# acoustic-token-modem

### Experimental acoustic modem for **direct machine-token** transmission

[![RESEARCH](https://img.shields.io/badge/status-RESEARCH-3b82f6?style=for-the-badge)](https://github.com/beyond-repair/ADL-Governance)
[![Claim level](https://img.shields.io/badge/claim-≤_1-yellow?style=for-the-badge)](CLAIM_STATUS.md)

</div>

---

## Claim cap (software / simulation)

**RUNNABLE SKETCH** — claim level **1** only. A stranger can clone `main`, `pip install -e ".[dev]"`, run `pytest tests/ -q`, and run `python experiments/baseline_fsk.py` for the FSK *simulation* roundtrip.

This is **not** hardware validation (M10), **not** a novelty claim, and **not** permission to report theoretical bitrate as achieved. PSK / QAM / OFDM modules are intentional placeholders. See [CLAIM_STATUS.md](CLAIM_STATUS.md).

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

Requires Python ≥ 3.10. Use a virtual environment. On PEP 668 systems (Debian/Ubuntu and many current images) `pip install` into the system interpreter is refused, and `python` / `pytest` may not be on `PATH` — only `python3`.

From a clone of this repository:

```bash
python3 -m venv .venv
.venv/bin/pip install -e ".[dev]"
.venv/bin/pytest tests/ -q
.venv/bin/python experiments/baseline_fsk.py
```

`baseline_fsk.py` is an offline AWGN simulation. It prints one JSON list (SNR, whether the token IDs reconstructed, and BER for that seed) and writes the same JSON to `benchmarks/results/baseline_fsk_awgn.json`. That file is a simulation record, not a speaker/mic measurement and not an achieved bitrate.

`experiments/baseline_psk.py` and `experiments/ofdm_density.py` print that those phases are not implemented and then exit. Do not treat them as modulators.

Hardware modes (`LIVE_MIC` / `LIVE_SPEAKER`) are stubs until M10.

CI: `.github/workflows/pytest.yml` runs the same `pytest tests/` suite. Green CI is **not** hardware validation and does **not** raise claim level. See [CLAIM_STATUS.md](CLAIM_STATUS.md).

Last verified Actions run before Sweep-110: **34068585607** (`success`, Sweep-092 head). Sweep-110 added GOVERNANCE.md and explicit UNSUPPORTED tokens only.

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
- Sweep-066 (2026-09-05): added pytest workflow; suite passed in CI (simulation only).
- Sweep-092 (2026-09-06): CLAIM_STATUS.md; no claim elevation.
- Sweep-110 (2026-09-07): GOVERNANCE.md; UNSUPPORTED tokens; no claim elevation.
- See [GOVERNANCE.md](GOVERNANCE.md), [docs/RESEARCH.md](docs/RESEARCH.md), [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), [SECURITY.md](docs/SECURITY.md)

---

<div align="center">

[Atomic Dream Labs](https://github.com/beyond-repair) · [ADL-Governance](https://github.com/beyond-repair/ADL-Governance)

</div>
