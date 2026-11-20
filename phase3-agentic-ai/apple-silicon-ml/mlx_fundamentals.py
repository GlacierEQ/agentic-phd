"""
MLX Fundamentals — Apple Silicon ML Array Operations & Device Management
Doctorate-level AI curriculum — Agentic PhD
"""
import mlx.core as mx
import time


def device_info():
    """Probe and report MLX device capabilities."""
    print("=== MLX Device Info ===")
    print(f"Default device: {mx.default_device()}")
    print(f"Metal available: {mx.metal.is_available()}")
    print("Metal version: (not exposed in this MLX build)")
    # List all available devices
    try:
        devices = mx.devices()
        print(f"Devices: {devices}")
    except AttributeError:
        print("Devices: (single default device model)")
    return mx.default_device()


def array_basics():
    """Demonstrate MLX array creation, operations, and lazy evaluation."""
    print("\n=== MLX Array Basics ===")

    # Create arrays (lazy by default)
    a = mx.array([1, 2, 3, 4, 5])
    b = mx.array([10, 20, 30, 40, 50])
    print(f"a = {a}")
    print(f"b = {b}")

    # Operations are lazy — they build a computation graph
    c = a + b
    print(f"a + b (lazy): {c}")  # forces evaluation

    # Matrix operations (GPU-accelerated)
    M = mx.ones((1000, 1000))
    N = mx.ones((1000, 1000))
    t0 = time.time()
    result = mx.matmul(M, N)
    mx.eval(result)  # force evaluation
    t1 = time.time()
    print(f"1000x1000 matmul: {t1-t0:.4f}s on {mx.default_device()}")

    # Reductions
    x = mx.random.normal((10000,))
    t0 = time.time()
    mean_val = mx.mean(x)
    mx.eval(mean_val)
    t1 = time.time()
    print(f"Mean of 10K elements: {mean_val.item():.6f} in {t1-t0:.4f}s")

    return result


def lazy_evaluation_demo():
    """Demonstrate MLX's lazy evaluation model."""
    print("\n=== Lazy Evaluation ===")

    # Build a computation graph without executing
    x = mx.array([1.0, 2.0, 3.0])
    y = x * 2 + 1
    z = mx.sin(y)
    # Nothing has executed yet — z is a lazy array

    # Force evaluation
    mx.eval(z)
    print(f"z = {z}")

    # Multiple outputs can be evaluated together
    a = mx.array([1.0, 2.0, 3.0])
    b = mx.array([4.0, 5.0, 6.0])
    c = a + b
    d = a * b
    mx.eval(c, d)  # evaluate both at once (more efficient)
    print(f"c = {c}, d = {d}")

    return z


def device_placement():
    """Demonstrate device placement and transfer."""
    print("\n=== Device Placement ===")

    # Default device is GPU on Apple Silicon
    print(f"Default device: {mx.default_device()}")

    # Create array on default device (GPU)
    gpu_arr = mx.array([1, 2, 3, 4, 5])
    print(f"Array device: {gpu_arr.device if hasattr(gpu_arr, 'device') else 'default (gpu)'}")

    # Operations stay on the same device
    result = gpu_arr * 2
    mx.eval(result)
    print(f"Result: {result}")

    return result


def gradient_demo():
    """Demonstrate automatic differentiation on GPU."""
    print("\n=== Automatic Differentiation ===")

    def f(x):
        return mx.sum(x ** 2)

    # Compute gradient
    grad_fn = mx.grad(f)
    x = mx.array([1.0, 2.0, 3.0])
    g = grad_fn(x)
    mx.eval(g)
    print(f"f(x) = sum(x^2), x = {x}")
    print(f"gradient = {g}")  # should be [2, 4, 6]

    # Value and gradient together
    vg_fn = mx.value_and_grad(f)
    val, grad = vg_fn(x)
    mx.eval(val, grad)
    print(f"value = {val.item()}, grad = {grad}")

    return g


def benchmark_suite():
    """Comprehensive MLX benchmark suite for M1 Air."""
    print("\n=== MLX Benchmark Suite (M1 Air) ===")
    device = mx.default_device()
    print(f"Running on: {device}")

    benchmarks = []

    # 1. Matrix multiplication (various sizes)
    for size in [256, 512, 1024, 2048]:
        A = mx.random.normal((size, size))
        B = mx.random.normal((size, size))
        mx.eval(A, B)

        # Warmup
        mx.eval(mx.matmul(A, B))

        # Timed run
        t0 = time.time()
        for _ in range(3):
            C = mx.matmul(A, B)
            mx.eval(C)
        t1 = time.time()
        avg = (t1 - t0) / 3
        gflops = (2 * size**3) / (avg * 1e9)
        benchmarks.append(("matmul", size, avg, gflops))
        print(f"  matmul {size}x{size}: {avg*1000:.1f}ms ({gflops:.1f} GFLOPS)")

    # 2. Element-wise operations
    x = mx.random.normal((10_000_000,))
    mx.eval(x)
    t0 = time.time()
    y = mx.exp(x) + mx.sin(x)
    mx.eval(y)
    t1 = time.time()
    print(f"  element-wise (10M): {(t1-t0)*1000:.1f}ms")

    # 3. Reduction
    t0 = time.time()
    s = mx.sum(x)
    mx.eval(s)
    t1 = time.time()
    print(f"  sum (10M): {(t1-t0)*1000:.1f}ms")

    # 4. Softmax
    logits = mx.random.normal((1000, 1000))
    mx.eval(logits)
    t0 = time.time()
    sm = mx.softmax(logits, axis=-1)
    mx.eval(sm)
    t1 = time.time()
    print(f"  softmax (1000x1000): {(t1-t0)*1000:.1f}ms")

    # 5. Memory bandwidth estimate
    size_mb = 256
    data = mx.random.normal((size_mb * 1024 * 1024 // 4,))
    mx.eval(data)
    t0 = time.time()
    copy = mx.array(data)
    mx.eval(copy)
    t1 = time.time()
    bw = (size_mb / (t1 - t0)) / 1024  # GB/s
    print(f"  memory bandwidth: {bw:.1f} GB/s (theoretical 68 GB/s)")

    return benchmarks


if __name__ == "__main__":
    device_info()
    array_basics()
    lazy_evaluation_demo()
    device_placement()
    gradient_demo()
    benchmark_suite()
    print("\n=== MLX Fundamentals Complete ===")
