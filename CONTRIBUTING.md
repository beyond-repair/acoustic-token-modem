# Contributing

This is a **research** repository under [ADL-Governance](https://github.com/beyond-repair/ADL-Governance).

## Rules

1. **No novelty claims** without prior-art analysis in `docs/RESEARCH.md` and measured benchmarks.
2. **Do not report theoretical bitrate as achieved bitrate.**
3. Every PR that changes performance claims must update `benchmarks/` with reproducible parameters.
4. Simulation-first; hardware PRs require documented device, SNR method, and distance.
5. Keep `network_access` out of the core path; this is a local acoustic protocol stack.
6. Prefer small, testable increments (M1 → M2 → …) over large unmeasured architectures.

## Tests

```bash
pip install -e ".[dev]"
pytest tests/ -q
```

The invariant `tokens_in == tokens_out` must hold for any accepted modulation path under the stated channel model.
