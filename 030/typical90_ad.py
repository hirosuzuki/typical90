# https://atcoder.jp/contests/typical90/tasks/typical90_ad

from typing import List

N, K = [int(x) for x in input().split()]


def solve(N: int, K: int):
    cs: List[int] = [0] * (N + 1)
    for i in range(2, N + 1):
        if cs[i] == 0:
            for j in range(i, N + 1, i):
                cs[j] += 1
    result = 0
    for i in range(2, N + 1):
        result += (cs[i] >= K)

    print(result)


solve(N, K)
