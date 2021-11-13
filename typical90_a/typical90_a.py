from typing import List

N, L = [int(_) for _ in input().split()]
K = int(input())
A = [int(_) for _ in input().split()]

def solve(N: int, L: int, K: int, A: List[int]) -> int:

    ds = [A[0]] + [A[i + 1] - A[i] for i in range(N - 1)] + [L - A[-1]]

    def check(v: int) -> bool:
        x = 0
        n = 0
        for d in ds:
            x += d
            if x >= v:
                x = 0
                n += 1
        return n >= K + 1

    hi = L
    lo = 0

    while lo + 1 < hi:
        m = (hi + lo) // 2
        if check(m):
            lo = m
        else:
            hi = m

    return lo


print(solve(N, L, K, A))
