# https://atcoder.jp/contests/typical90/tasks/typical90_cc

from typing import List

N, K = [int(x) for x in input().split()]
AB = [[int(x) for x in input().split()] for _ in range(N)]

def solve(N: int, K: int, AB: List[List[int]]):
    cs = [[0] * 5002 for _ in range(5002)]
    for a, b in AB:
        cs[b][a] += 1

    for i in range(5002):
        for j in range(5001):
            cs[i][j + 1] += cs[i][j]

    for j in range(5002):
        for i in range(5001):
            cs[i + 1][j] += cs[i][j]

    result = 0
    for i in range(0, 5001 - K):
        for j in range(0, 5001 - K):
            r = cs[i][j] - cs[i][j + K + 1] - cs[i + K + 1][j] + cs[i + K + 1][j + K + 1]
            result = max(result, r)
    print(result)

solve(N, K, AB)


