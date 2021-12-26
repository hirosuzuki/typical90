# https://atcoder.jp/contests/typical90/tasks/typical90_ax

from typing import List

N, L = [int(x) for x in input().split()]


def solve(N: int, L: int):
    M = 10**9+7
    dp: List[int] = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        dp[i] = (dp[i - 1] + (dp[i - L] if i - L >= 0 else 0)) % M
    result = dp[N]
    print(result)


solve(N, L)
