# https://atcoder.jp/contests/typical90/tasks/typical90_l

from typing import List

from collections import defaultdict


class UnionFind():
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

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


H, W = [int(e) for e in input().split()]
Q = int(input())
q = [[int(e) for e in input().split()] for _ in range(Q)]


def solve(H: int, W: int, Q: int, q: List[List[int]]):
    w, h = W + 2, H + 2
    cs = [[0] * w for _ in range(h)]
    uf = UnionFind(w * h)
    for i in range(Q):
        if q[i][0] == 1:
            x1, y1 = q[i][2], q[i][1]
            p1 = y1 * w + x1
            cs[y1][x1] = 1
            for dx, dy in ((-1, 0), (+1, 0), (0, -1), (0, +1)):
                x2, y2 = x1 + dx, y1 + dy
                if cs[y2][x2]:
                    p2 = y2 * w + x2
                    uf.union(p1, p2)
        if q[i][0] == 2:
            x1, y1 = q[i][2], q[i][1]
            x2, y2 = q[i][4], q[i][3]
            p1 = y1 * w + x1
            p2 = y2 * w + x2
            if cs[y1][x1] and cs[y2][x2] and uf.same(p1, p2):
                print("Yes")
            else:
                print("No")


solve(H, W, Q, q)
