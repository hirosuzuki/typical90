# https://atcoder.jp/contests/typical90/tasks/typical90_aw

from typing import List, Set

N, M = [int(x) for x in input().split()]
CLR = [[int(x) for x in input().split()] for _ in range(M)]


class UnionFind:

    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]


def solve(N: int, M: int, CLR: List[List[int]]):
    clr = sorted(CLR)
    uf = UnionFind(N + 1)
    result = 0
    cs: Set[int] = set()
    for c, l, r in clr:
        if uf.find(l - 1) != uf.find(r):
            uf.union(l - 1, r)
            cs.add(l - 1)
            cs.add(r)
            result += c
    if sum(x < 0 for x in uf.parents) != 1:
        result = -1
    print(result)


solve(N, M, CLR)
