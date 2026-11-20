"""
MLX Deep Dive — PhD-Level Apple Silicon ML Research
Doctorate-level AI curriculum — Agentic PhD
"""
import mlx.core as mx
import mlx.nn as nn
import time
import json


def section(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


# =====================================================================
# 1. MLX ARCHITECTURE & INTERNALS
# =====================================================================

def mlx_architecture():
    section("1. MLX ARCHITECTURE & INTERNALS")

    print("""
MLX Design Philosophy (Apple, 2023):
  - Array framework for Apple Silicon (M1-M5)
  - Inspired by NumPy, PyTorch, JAX
  - Key innovation: lazy evaluation + unified memory + Metal GPU

Core Design Principles:
  1. Unified Memory: CPU and GPU share the same physical memory
     - No explicit data transfer (no .to('cuda') needed)
     - Zero-copy between CPU/GPU operations
     - Memory bandwidth: 68 GB/s (M1) to 400+ GB/s (M4 Max)

  2. Lazy Evaluation:
     - Operations build a computation graph
     - Nothing executes until mx.eval() or .item() is called
     - Enables graph optimization and fusion
     - Multiple outputs evaluated together (more efficient)

  3. Composable Function Transforms:
     - mx.grad() — automatic differentiation
     - mx.vmap() — vectorization
     - mx.compile() — JIT compilation
     - mx.checkpoint() — gradient checkpointing

  4. Metal GPU Backend:
     - All operations dispatch to Metal compute shaders
     - Custom Metal kernels supported
     - GPU memory managed by unified memory (no separate VRAM)
""")

    # Probe the actual device
    device = mx.default_device()
    print(f"  Current device: {device}")
    print(f"  Metal available: {mx.metal.is_available()}")
    print(f"  Metal version: (not exposed in this MLX build)")

    # Memory info
    try:
        print(f"  Active memory: {mx.metal.get_active_memory() / 1e9:.2f} GB")
        print(f"  Peak memory: {mx.metal.get_peak_memory() / 1e9:.2f} GB")
        print(f"  Cache memory: {mx.metal.get_cache_memory() / 1e9:.2f} GB")
    except Exception as e:
        print(f"  Memory info: {e}")

    return device


# =====================================================================
# 2. LAZY EVALUATION DEEP DIVE
# =====================================================================

def lazy_evaluation_deep():
    section("2. LAZY EVALUATION DEEP DIVE")

    print("""
Lazy Evaluation Model:
  - Operations are NOT executed immediately
  - Instead, a computation graph (DAG) is built
  - Execution is deferred until:
    a) mx.eval(array) is called
    b) .item() is called (scalar extraction)
    c) print() forces evaluation
    d) Array is passed to another framework

Benefits:
  1. Graph optimization: MLX can fuse operations
  2. Memory efficiency: intermediate results can be freed
  3. Batch evaluation: multiple outputs evaluated together
  4. JIT compilation: entire graph compiled to Metal

Key Functions:
  - mx.eval(*arrays): Force evaluation of one or more arrays
  - mx.compile(fn): JIT compile a function
  - mx.checkpoint(fn): Gradient checkpointing
""")

    # Demonstrate lazy evaluation
    x = mx.array([1.0, 2.0, 3.0])
    y = x * 2 + 1
    z = mx.sin(y)
    w = mx.cos(z)
    # Nothing has executed yet!

    # Time lazy vs eager
    t0 = time.time()
    mx.eval(w)  # Forces entire chain: x -> y -> z -> w
    t1 = time.time()
    print(f"  Full chain eval (4 ops): {(t1-t0)*1000:.3f}ms")

    # Batch evaluation is more efficient
    a = mx.random.normal((1000, 1000))
    b = mx.random.normal((1000, 1000))
    c = a + b
    d = a * b
    e = a @ b  # matmul

    t0 = time.time()
    mx.eval(c, d, e)  # Evaluate all at once
    t1 = time.time()
    print(f"  Batch eval (3 ops, 1000x1000): {(t1-t0)*1000:.1f}ms")

    # JIT compilation
    print("\n  JIT Compilation:")

    def f(x):
        return mx.sin(x) + mx.cos(x) * 2

    compiled_f = mx.compile(f)
    x = mx.random.normal((10000,))

    # Warmup
    mx.eval(compiled_f(x))

    t0 = time.time()
    for _ in range(100):
        mx.eval(compiled_f(x))
    t1 = time.time()
    print(f"  Compiled (100 calls): {(t1-t0)*1000:.1f}ms")

    t0 = time.time()
    for _ in range(100):
        mx.eval(f(x))
    t1 = time.time()
    print(f"  Uncompiled (100 calls): {(t1-t0)*1000:.1f}ms")


# =====================================================================
# 3. FUNCTION TRANSFORMS
# =====================================================================

def function_transforms():
    section("3. FUNCTION TRANSFORMS")

    print("""
MLX Function Transforms (JAX-inspired):
  - mx.grad(fn): Compute gradient of fn
  - mx.value_and_grad(fn): Return both value and gradient
  - mx.vmap(fn): Vectorize a function over a batch dimension
  - mx.compile(fn): JIT compile to Metal
  - mx.checkpoint(fn): Gradient checkpointing (memory vs compute tradeoff)
""")

    # Gradient
    def mse_loss(params, x, y):
        pred = x @ params['W'] + params['b']
        return mx.mean((pred - y) ** 2)

    params = {'W': mx.random.normal((4, 1)), 'b': mx.zeros((1,))}
    x = mx.random.normal((32, 4))
    y = mx.random.normal((32, 1))

    grad_fn = mx.value_and_grad(mse_loss)
    loss, grads = grad_fn(params, x, y)
    mx.eval(loss, *grads.values())
    print(f"  MSE loss: {loss.item():.4f}")
    print(f"  Grad W shape: {grads['W'].shape}")
    print(f"  Grad b shape: {grads['b'].shape}")

    # vmap (vectorization)
    def single_forward(x, w):
        return x @ w

    batched_forward = mx.vmap(single_forward, in_axes=(0, None))
    X = mx.random.normal((8, 4))
    w = mx.random.normal((4, 1))
    out = batched_forward(X, w)
    mx.eval(out)
    print(f"  vmap output shape: {out.shape} (batched 8 samples)")

    # Compile
    def relu(x):
        return mx.maximum(x, 0)

    compiled_relu = mx.compile(relu)
    x = mx.random.normal((10000,))
    mx.eval(compiled_relu(x))
    print(f"  compiled relu: OK")

    return loss


# =====================================================================
# 4. NEURAL NETWORK MODULES
# =====================================================================

def neural_network_modules():
    section("4. NEURAL NETWORK MODULES (mlx.nn)")

    print("""
mlx.nn provides PyTorch-like neural network modules:
  - nn.Linear, nn.Conv2d, nn.Embedding
  - nn.LayerNorm, nn.BatchNorm, nn.GroupNorm
  - nn.ReLU, nn.GELU, nn.SiLU, nn.Softmax
  - nn.Sequential, nn.ModuleList
  - nn.TransformerEncoder, nn.TransformerDecoder
  - nn.LSTM, nn.GRU
""")

    # Build a small transformer
    class MiniTransformer(nn.Module):
        def __init__(self, d_model=64, n_heads=4, n_layers=2):
            super().__init__()
            self.embedding = nn.Embedding(1000, d_model)
            self.pos_encoding = nn.Embedding(512, d_model)
            self.layers = [nn.TransformerEncoderLayer(d_model, n_heads) for _ in range(n_layers)]
            self.norm = nn.LayerNorm(d_model)
            self.head = nn.Linear(d_model, 1000)

        def __call__(self, x):
            seq_len = x.shape[1]
            pos = mx.arange(seq_len)
            x = self.embedding(x) + self.pos_encoding(pos)
            for layer in self.layers:
                x = layer(x, None)
            x = self.norm(x)
            return self.head(x)

    model = MiniTransformer()
    mx.eval(model.parameters())

    # Count parameters
    params = model.parameters()
    total = sum(p.size for p in _flatten_params(params))
    print(f"  MiniTransformer params: {total:,}")

    # Forward pass
    x = mx.array([[1, 2, 3, 4, 5]])
    t0 = time.time()
    out = model(x)
    mx.eval(out)
    t1 = time.time()
    print(f"  Forward pass: {(t1-t0)*1000:.1f}ms, output shape: {out.shape}")

    # Training step
    def loss_fn(model, x, y):
        logits = model(x)
        return mx.mean(nn.losses.cross_entropy(logits.reshape(-1, 1000), y.reshape(-1)))

    import mlx.optimizers as optim
    optimizer = optim.Adam(learning_rate=1e-3)
    loss_and_grad = nn.value_and_grad(model, loss_fn)

    y = mx.array([[2, 3, 4, 5, 6]])
    loss, grads = loss_and_grad(model, x, y)
    optimizer.update(model, grads)
    mx.eval(model.parameters(), loss)
    print(f"  Training step loss: {loss.item():.4f}")

    return model


def _flatten_params(params):
    """Flatten nested parameter dict."""
    flat = []
    if isinstance(params, dict):
        for v in params.values():
            flat.extend(_flatten_params(v))
    elif isinstance(params, list):
        for v in params:
            flat.extend(_flatten_params(v))
    elif hasattr(params, 'size'):
        flat.append(params)
    return flat


# =====================================================================
# 5. MEMORY MANAGEMENT
# =====================================================================

def memory_management():
    section("5. MEMORY MANAGEMENT")

    print("""
MLX Memory Model (Unified Memory):
  - CPU and GPU share the same physical memory
  - No explicit .to('gpu') or .to('cpu') needed
  - Memory is allocated lazily and freed when arrays go out of scope
  - mx.metal provides memory introspection

Key Functions:
  - mx.metal.get_active_memory(): Currently allocated
  - mx.metal.get_peak_memory(): Peak allocation
  - mx.metal.get_cache_memory(): Cached (reusable) memory
  - mx.metal.clear_cache(): Free cached memory
  - mx.metal.set_memory_limit(bytes): Set memory limit
  - mx.metal.set_cache_limit(bytes): Set cache limit

Memory Optimization Strategies:
  1. Use quantized models (4-bit, 8-bit) — 4-8x memory reduction
  2. Gradient checkpointing — trade compute for memory
  3. Clear cache between batches
  4. Use smaller batch sizes
  5. Use mx.eval() to free intermediate results
""")

    # Memory introspection
    mx.metal.clear_cache()
    print(f"  Active: {mx.metal.get_active_memory() / 1e6:.1f} MB")
    print(f"  Peak: {mx.metal.get_peak_memory() / 1e6:.1f} MB")
    print(f"  Cache: {mx.metal.get_cache_memory() / 1e6:.1f} MB")

    # Allocate a large array
    big = mx.random.normal((4096, 4096))
    mx.eval(big)
    print(f"\n  After allocating 4096x4096 (64MB):")
    print(f"  Active: {mx.metal.get_active_memory() / 1e6:.1f} MB")
    print(f"  Peak: {mx.metal.get_peak_memory() / 1e6:.1f} MB")

    # Free it
    del big
    mx.metal.clear_cache()
    print(f"\n  After del + clear_cache:")
    print(f"  Active: {mx.metal.get_active_memory() / 1e6:.1f} MB")
    print(f"  Cache: {mx.metal.get_cache_memory() / 1e6:.1f} MB")

    # Memory limits
    print(f"\n  Memory limit: (set via mx.metal.set_memory_limit())")
    print(f"  Cache limit: (set via mx.metal.set_cache_limit())")


# =====================================================================
# 6. METAL GPU KERNELS
# =====================================================================

def metal_kernels():
    section("6. CUSTOM METAL GPU KERNELS")

    print("""
MLX supports custom Metal kernels for operations not in the standard library.

Custom Kernel API:
  - mx.fast.metal_kernel(name, input_names, output_names, source)
  - Write Metal Shading Language (MSL) code
  - Compile and execute on GPU

Use Cases:
  - Fused operations (reduce memory bandwidth)
  - Custom activation functions
  - Specialized quantization/dequantization
  - Flash attention implementations

Example: Custom element-wise kernel
""")

    # Simple custom kernel: element-wise square
    try:
        kernel = mx.fast.metal_kernel(
            name="square_kernel",
            input_names=["inp"],
            output_names=["out"],
            source="""
                uint idx = thread_position_in_grid.x;
                out[idx] = inp[idx] * inp[idx];
            """
        )

        x = mx.array([1.0, 2.0, 3.0, 4.0, 5.0])
        out = kernel(
            inputs=[x],
            output_shapes=[(5,)],
            output_dtypes=[mx.float32],
            grid=(5, 1, 1),
            threadgroup=(5, 1, 1)
        )
        mx.eval(out[0])
        print(f"  Input:  {x}")
        print(f"  Output: {out[0]}")
        print("  Custom Metal kernel: OK")
    except Exception as e:
        print(f"  Custom kernel error: {e}")
        print("  (May require specific MLX version or Metal toolchain)")


# =====================================================================
# 7. LLM INFERENCE ON GPU
# =====================================================================

def llm_inference():
    section("7. LLM INFERENCE ON GPU (mlx_lm)")

    print("""
mlx_lm provides LLM inference on Apple Silicon GPU:

Supported Models:
  - Llama 2/3/3.1/3.2 (1B-70B)
  - Mistral/Mixtral
  - Phi-2/3/3.5
  - Qwen 1.5/2/2.5
  - Gemma/Gemma 2
  - DeepSeek
  - And many more (HuggingFace compatible)

Quantization:
  - 4-bit (Q4): ~4x memory reduction, minimal quality loss
  - 8-bit (Q8): ~2x memory reduction, near-lossless
  - Mixed precision: different bits per layer

Memory Requirements (M1 Air, 16 GB unified):
  - 3B model Q4: ~2 GB (fits easily)
  - 7B model Q4: ~4 GB (fits with headroom)
  - 13B model Q4: ~7 GB (tight, may swap)
  - 70B model Q4: ~35 GB (needs M-series with 64+ GB)

Inference Speed (M1, 7-core GPU, estimated):
  - 3B Q4: ~40-60 tok/s
  - 7B Q4: ~20-30 tok/s
  - 13B Q4: ~10-15 tok/s

Key Commands:
  mlx_lm.generate --model <model> --prompt <text>
  mlx_lm.chat --model <model>
  mlx_lm.server --model <model>  (OpenAI-compatible API)
  mlx_lm.convert --hf-path <hf_model> -q  # Convert to MLX format
""")

    # Check what models are cached
    import os
    cache_dir = os.path.expanduser("~/.cache/huggingface/hub")
    if os.path.exists(cache_dir):
        models = [d for d in os.listdir(cache_dir) if d.startswith("models--")]
        print(f"  Cached models: {len(models)}")
        for m in models[:5]:
            print(f"    - {m.replace('models--', '').replace('--', '/')}")
    else:
        print("  No cached models found")

    # Check mlx_lm server capability
    print("\n  mlx_lm.server provides OpenAI-compatible API at localhost:8080")
    print("  This can replace OpenAI API calls in the mainframe stack")


# =====================================================================
# 8. PERFORMANCE OPTIMIZATION FOR M1 AIR
# =====================================================================

def performance_optimization():
    section("8. PERFORMANCE OPTIMIZATION FOR M1 AIR")

    print("""
M1 Air Specific Optimizations:

1. Thermal Management (fanless design):
   - Peak performance: ~2 minutes before thermal throttle
   - Sustained: ~80% of peak after throttle
   - GPU compute is MORE thermally efficient than CPU for ML
   - Use workload scheduling: burst compute, then idle

2. Memory Optimization:
   - Unified memory = CPU + GPU + ANE share 16 GB
   - Quantized models (4-bit) reduce memory 4x
   - Clear cache between batches: mx.metal.clear_cache()
   - Set memory limits: mx.metal.set_memory_limit(bytes)

3. Compute Scheduling:
   - GPU for: matrix ops, convolutions, attention, inference
   - CPU for: data loading, preprocessing, I/O
   - ANE for: small models via CoreML (classification, embedding)
   - Avoid: CPU-only inference when GPU is available

4. Batch Size Tuning:
   - M1 Air: optimal batch size 1-4 for 7B models
   - Larger batches → more memory, may swap
   - Use gradient accumulation for training

5. Power Efficiency:
   - M1 Air: ~15W under load (no fan)
   - GPU compute: ~2-3x more efficient per FLOP than CPU
   - Battery: ~18 hours idle, ~8-10 hours under MLX inference

6. Swap Avoidance:
   - Current swap: 9 GB used (CRITICAL)
   - Free memory before inference: close heavy apps
   - Use 4-bit quantized models to minimize memory
   - Monitor: vm_stat, sysctl vm.swapusage
""")

    # Benchmark: CPU vs GPU for matrix multiply
    print("  CPU vs GPU Benchmark:")

    # GPU (MLX default)
    A = mx.random.normal((2048, 2048))
    B = mx.random.normal((2048, 2048))
    mx.eval(A, B)

    t0 = time.time()
    for _ in range(5):
        C = mx.matmul(A, B)
        mx.eval(C)
    t1 = time.time()
    gpu_time = (t1 - t0) / 5
    print(f"  GPU (MLX): {gpu_time*1000:.1f}ms per 2048x2048 matmul")

    # Estimate CPU time (numpy if available)
    try:
        import numpy as np
        A_np = np.random.randn(2048, 2048).astype(np.float32)
        B_np = np.random.randn(2048, 2048).astype(np.float32)
        t0 = time.time()
        for _ in range(3):
            C_np = A_np @ B_np
        t1 = time.time()
        cpu_time = (t1 - t0) / 3
        print(f"  CPU (numpy): {cpu_time*1000:.1f}ms per 2048x2048 matmul")
        print(f"  GPU speedup: {cpu_time/gpu_time:.1f}x")
    except ImportError:
        print("  (numpy not available for CPU comparison)")


# =====================================================================
# 9. INTEGRATION WITH MAINFRAME STACK
# =====================================================================

def mainframe_integration():
    section("9. MAINFRAME STACK INTEGRATION")

    print("""
M1 Air as Controller Node — GPU Integration Points:

1. Local Inference Server (mlx_lm.server):
   - OpenAI-compatible API at localhost:8080
   - Can serve as fallback when cloud APIs are down
   - Models: 3B-7B quantized (fits in 16 GB with headroom)

2. Embedding Generation:
   - Use MLX for local embedding computation
   - Faster than API calls for small batches
   - Models: all-MiniLM-L6-v2, bge-small-en

3. Agent Tool Execution:
   - MLX for local code analysis, summarization
   - Reduces API costs and latency
   - Privacy: data stays on device

4. Monitoring & Health:
   - GPU utilization via mx.metal.get_active_memory()
   - Thermal monitoring via powermetrics
   - Memory pressure via vm_stat

5. Model Routing (from optimization playbook):
   - Small tasks (< 1K tokens): local MLX inference
   - Medium tasks (1K-10K): cloud API (kilo.ai)
   - Large tasks (> 10K): cloud API with larger context

Recommended Model Stack for M1 Air:
  - Primary: mlx-community/Llama-3.2-3B-Instruct-4bit (~2 GB)
  - Embedding: mlx-community/all-MiniLM-L6-v2-4bit
  - Code: mlx-community/Qwen2.5-Coder-3B-Instruct-4bit
  - Fallback: mlx-community/Phi-3.5-mini-instruct-4bit
""")

    # Check if mlx_lm server can be started
    print("  To start local inference server:")
    print("  ~/Library/Python/3.13/mx-env/bin/python3 -m mlx_lm.server \\")
    print("    --model mlx-community/Llama-3.2-3B-Instruct-4bit \\")
    print("    --port 8080")


# =====================================================================
# 10. BENCHMARK RESULTS
# =====================================================================

def run_benchmarks():
    section("10. COMPREHENSIVE BENCHMARKS")

    results = {}

    # Matmul scaling
    print("\n  Matrix Multiplication (GPU):")
    for size in [256, 512, 1024, 2048]:
        A = mx.random.normal((size, size))
        B = mx.random.normal((size, size))
        mx.eval(A, B)
        mx.eval(mx.matmul(A, B))  # warmup

        t0 = time.time()
        for _ in range(5):
            C = mx.matmul(A, B)
            mx.eval(C)
        t1 = time.time()
        avg = (t1 - t0) / 5
        gflops = (2 * size**3) / (avg * 1e9)
        results[f"matmul_{size}"] = {"ms": avg*1000, "gflops": gflops}
        print(f"    {size}x{size}: {avg*1000:.1f}ms ({gflops:.1f} GFLOPS)")

    # Softmax
    print("\n  Softmax (GPU):")
    for size in [1000, 4096]:
        x = mx.random.normal((size, size))
        mx.eval(x)
        t0 = time.time()
        for _ in range(5):
            s = mx.softmax(x, axis=-1)
            mx.eval(s)
        t1 = time.time()
        avg = (t1 - t0) / 5
        results[f"softmax_{size}"] = {"ms": avg*1000}
        print(f"    {size}x{size}: {avg*1000:.1f}ms")

    # Attention (scaled dot-product)
    print("\n  Scaled Dot-Product Attention (GPU):")
    for seq_len in [128, 512, 1024]:
        Q = mx.random.normal((1, 8, seq_len, 64))  # batch=1, heads=8, seq, dim=64
        K = mx.random.normal((1, 8, seq_len, 64))
        V = mx.random.normal((1, 8, seq_len, 64))
        mx.eval(Q, K, V)

        def attention(Q, K, V):
            scale = 1.0 / (64 ** 0.5)
            scores = (Q @ K.transpose(0, 1, 3, 2)) * scale
            weights = mx.softmax(scores, axis=-1)
            return weights @ V

        mx.eval(attention(Q, K, V))  # warmup

        t0 = time.time()
        for _ in range(5):
            out = attention(Q, K, V)
            mx.eval(out)
        t1 = time.time()
        avg = (t1 - t0) / 5
        results[f"attention_{seq_len}"] = {"ms": avg*1000}
        print(f"    seq={seq_len}: {avg*1000:.1f}ms")

    # Memory bandwidth
    print("\n  Memory Bandwidth:")
    size_mb = 512
    data = mx.random.normal((size_mb * 1024 * 1024 // 4,))
    mx.eval(data)
    t0 = time.time()
    for _ in range(5):
        copy = mx.array(data)
        mx.eval(copy)
    t1 = time.time()
    avg = (t1 - t0) / 5
    bw = size_mb / (avg * 1024)  # GB/s
    results["memory_bandwidth"] = {"gbps": bw}
    print(f"    {size_mb}MB copy: {avg*1000:.1f}ms ({bw:.1f} GB/s, theoretical 68 GB/s)")

    # Save results
    with open("/tmp/mlx_benchmark_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n  Results saved to /tmp/mlx_benchmark_results.json")

    return results


# =====================================================================
# MAIN
# =====================================================================

if __name__ == "__main__":
    print("MLX Deep Dive — PhD-Level Apple Silicon ML Research")
    print(f"MLX version: {mx.__version__}")
    print(f"Python: {__import__('sys').version}")

    mlx_architecture()
    lazy_evaluation_deep()
    function_transforms()
    neural_network_modules()
    memory_management()
    metal_kernels()
    llm_inference()
    performance_optimization()
    mainframe_integration()
    run_benchmarks()

    print("\n" + "="*60)
    print("  MLX Deep Dive Complete")
    print("="*60)
