# Architecture

## Pipeline

```text
TokenSequence (int IDs)
    → TokenMapper / optional compression
    → Packet (header + payload + FEC + CRC)
    → SymbolMapper
    → Modulator (FSK baseline → PSK/QAM/OFDM later)
    → AcousticChannel (sim or device)
    → Demodulator
    → FEC decode
    → Packet verify (CRC / sequence)
    → TokenSequence
```

## Layers

| Layer | Responsibility |
|-------|----------------|
| Tokenizer abstraction | Vocab-agnostic integer IDs; `bits_per_token = ceil(log2(V))` |
| Protocol | Framing, session, sequence, fragmentation |
| Coding | FEC, interleaving, symbol alphabet |
| Modulation | Waveform synthesis / detection |
| Channel | Simulation models or hardware abstraction |
| Metrics | BER, PER, throughput, token density, latency |

## Modes

`SIMULATION` · `AUDIO_FILE` · `LOOPBACK` · `LIVE_MIC` · `LIVE_SPEAKER`

Core development targets **SIMULATION** until M10.

## Integrity vs authentication

- **CRC** — accidental corruption  
- **Cryptographic auth** (optional, later) — intentional modification  

Do not conflate the two (`docs/SECURITY.md`).
