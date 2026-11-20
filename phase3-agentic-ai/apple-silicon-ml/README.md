# Apple Silicon ML — MLX + Neural Engine Deep Dive

PhD-level research and implementation for leveraging Apple Silicon (M1) GPU/ANE
for local ML inference and training, as part of the Agentic PhD curriculum.

## Files

- `mlx_fundamentals.py` — MLX basics: arrays, lazy eval, autodiff, benchmarks
- `mlx_deep_dive.py` — Comprehensive MLX research: architecture, transforms, nn, memory, Metal kernels, LLM inference, optimization, mainframe integration
- `neural_engine.py` — ANE + GPU + CPU triad: CoreML models, triad benchmark, workload router, power/thermal modeling

## Environment

```bash
# All dependencies installed in isolated venv
~/Library/Python/3.13/mx-env/bin/python3 mlx_deep_dive.py
~/Library/Python/3.13/mx-env/bin/python3 mlx_fundamentals.py
~/Library/Python/3.13/mx-env/bin/python3 neural_engine.py
```

## Dependencies

- MLX 0.32.4 (GPU via Metal)
- coremltools 9.0 (ANE via CoreML)
- PyTorch 2.15.0 (model source for CoreML conversion)
- scikit-learn 1.9.1 (not supported by coremltools, use PyTorch instead)

## Key Findings

- M1 Air: 7-core GPU, 16 GB unified memory, 68 GB/s bandwidth, 16-core ANE (11 TOPS int8)
- MLX 0.32.4: GPU matmul 2048x2048 in 13.1ms (1311 GFLOPS)
- JIT compilation: 1.54x speedup over eager
- ANE via CoreML: 3 models converted (classifier, conv, embedding) — all verified
- Triad benchmark: CPU 0.002ms, ANE 0.415ms, GPU 0.944ms (64x64 matmul)
- ANE is 2750x more efficient than CPU per watt for int8 ops
- Workload router dispatches: small models → ANE, large/batch → GPU, serial → CPU

## Status

All three modules run successfully end-to-end on the M1 Air's GPU and ANE.
