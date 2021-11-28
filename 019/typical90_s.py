# https://atcoder.jp/contests/typical90/tasks/typical90_s

from typing import List

N = int(input())
A = [int(x) for x in input().split()]


def solve(N: int, A: List[int]):
    B = 10**10
    dp: List[List[int]] = [[B for _ in range(N * 2)] for _ in range(N * 2 - 1)]
    for i in range(1, N * 2, 2):
        for j in range(N * 2 - i):
            if i == 1:
                dp[j][j + i] = abs(A[j + i] - A[j])
            else:
                dp[j][j + i] = min(
                    min(dp[j][k - 1] + dp[k][j + i]
                        for k in range(j, j + i + 1, 2)),
                    abs(A[j + i] - A[j]) + dp[j + 1][j + i - 1]
                )
    result = dp[0][N * 2 - 1]
    print(result)


solve(N, A)
