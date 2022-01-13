# https://atcoder.jp/contests/typical90/tasks/typical90_cb

from typing import List

N, D = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]


def solve(N: int, D: int, A: List[int]):
    result = 2**D
    for i in range(1, 2**N):
        y = 0
        bc = 0
        for j in range(N):
            if (1 << j) & i:
                y |= A[j]
                bc += 1
        r = 0
        for j in range(D):
            if (1 << j) & y == 0:
                r += 1
        if bc % 2 == 0:
            result += 2**r
        else:
            result -= 2**r
    print(result)


solve(N, D, A)
