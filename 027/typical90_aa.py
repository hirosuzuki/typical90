# https://atcoder.jp/contests/typical90/tasks/typical90_aa

from typing import List, Set

N = int(input())
S = [input() for _ in range(N)]


def solve(N: int, S: List[str]):
    rs: Set[str] = set()
    for n, s in enumerate(S):
        if s not in rs:
            rs.add(s)
            print(n + 1)


solve(N, S)
