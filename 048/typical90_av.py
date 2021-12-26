# https://atcoder.jp/contests/typical90/tasks/typical90_av

from typing import List

N, K = [int(x) for x in input().split()]
AB = [[int(x) for x in input().split()] for _ in range(N)]


def solve(N: int, K: int, AB: List[List[int]]):
    xs = [b for a, b in AB] + [a - b for a, b in AB]
    xs.sort()
    result = sum(xs[-K:])
    print(result)


solve(N, K, AB)
