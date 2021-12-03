# https://atcoder.jp/contests/typical90/tasks/typical90_x

from typing import List

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]


def solve(N: int, K: int, A: List[int], B: List[int]):
    s = sum(abs(a - b) for a, b in zip(A, B))
    if s <= K and (s - K) % 2 == 0:
        print("Yes")
    else:
        print("No")


solve(N, K, A, B)
