"""
Linear Algebra & Geometry — Spectral Theory
Doctorate-level AI curriculum — Agentic PhD
"""
import math
from typing import List, Tuple, Callable


def eigenvalues_2x2(a, b, c, d) -> Tuple[complex, complex]:
    """Eigenvalues of [[a,b],[c,d]] via characteristic polynomial."""
    trace = a + d
    det = a * d - b * c
    disc = trace**2 - 4 * det
    if disc >= 0:
        return ((trace + math.sqrt(disc)) / 2, (trace - math.sqrt(disc)) / 2)
    real, imag = trace / 2, math.sqrt(-disc) / 2
    return (complex(real, imag), complex(real, -imag))


def svd_2x2(a, b, c, d) -> Tuple[List[float], List[List[float]], List[List[float]]]:
    """Simplified SVD for 2x2: returns singular values."""
    # A^T A
    ata = [[a*a + c*c, a*b + c*d], [a*b + c*d, b*b + d*d]]
    ev1, ev2 = eigenvalues_2x2(ata[0][0], ata[0][1], ata[1][0], ata[1][1])
    s1 = math.sqrt(max(0, ev1.real if isinstance(ev1, complex) else ev1))
    s2 = math.sqrt(max(0, ev2.real if isinstance(ev2, complex) else ev2))
    return sorted([s1, s2], reverse=True), [], []


def matrix_rank(mat: List[List[float]], tol: float = 1e-9) -> int:
    """Rank via Gaussian elimination with partial pivoting."""
    rows = [r[:] for r in mat]
    m, n = len(rows), len(rows[0]) if rows else 0
    rank = 0
    for col in range(n):
        pivot = next((r for r in range(rank, m) if abs(rows[r][col]) > tol), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        pv = rows[rank][col]
        rows[rank] = [x / pv for x in rows[rank]]
        for r in range(m):
            if r != rank and abs(rows[r][col]) > tol:
                f = rows[r][col]
                rows[r] = [rows[r][j] - f * rows[rank][j] for j in range(n)]
        rank += 1
        if rank == m:
            break
    return rank


def frobenius_norm(mat: List[List[float]]) -> float:
    return math.sqrt(sum(x*x for row in mat for x in row))


def spectral_norm_approx(mat: List[List[float]]) -> float:
    """Approximate spectral norm (largest singular value) via power iteration."""
    n = len(mat[0]) if mat else 0
    v = [1.0 / math.sqrt(n)] * n
    for _ in range(50):
        # Av
        Av = [sum(mat[i][j] * v[j] for j in range(n)) for i in range(len(mat))]
        # A^T (Av)
        AtAv = [sum(mat[i][j] * Av[i] for i in range(len(mat))) for j in range(n)]
        norm = math.sqrt(sum(x*x for x in AtAv))
        v = [x / norm for x in AtAv]
    Av = [sum(mat[i][j] * v[j] for j in range(n)) for i in range(len(mat))]
    return math.sqrt(sum(x*x for x in Av))


if __name__ == "__main__":
    print("=== Linear Algebra: Spectral Theory ===")
    ev = eigenvalues_2x2(3, 1, 2, 4)
    print(f"Eigenvalues [[3,1],[2,4]]: {ev}")
    svs = svd_2x2(3, 1, 2, 4)
    print(f"Singular values: {svs[0]}")
    r = matrix_rank([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"Rank of singular matrix: {r}")
    fn = frobenius_norm([[3, 1], [2, 4]])
    print(f"Frobenius norm: {fn:.4f}")
    sn = spectral_norm_approx([[3, 1], [2, 4]])
    print(f"Spectral norm (approx): {sn:.4f}")
    print("✓ Linear Algebra module complete.")
