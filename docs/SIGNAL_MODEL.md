# Signal model

## Baseline (M3): binary FSK

- Two tones within a configurable band (default near-ultrasonic-friendly ranges are experimental only; audible bands allowed for lab speakers).
- Symbol duration `T_sym`; bit rate ≈ `1/T_sym` for binary FSK before coding.
- Preamble for acquisition.

## Later schemes

PSK / QPSK / QAM / OFDM are implemented as **separate modules** and compared under **identical** simulated channels. OFDM is not assumed superior.

## Channel (simulation)

Configurable: AWGN SNR, multipath taps, simple reverberation scalar, frequency offset, timing offset, optional clipping. See `src/acoustic_token_modem/channel/`.

Physical claims require hardware and method documentation.
