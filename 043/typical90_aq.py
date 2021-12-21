# https://atcoder.jp/contests/typical90/tasks/typical90_aq

from typing import List, Deque, Tuple
from collections import deque

H, W = [int(x) for x in input().split()]
RS, CS = [int(x) for x in input().split()]
RT, CT = [int(x) for x in input().split()]
S = [input() for _ in range(H)]

def solve0(H: int, W: int, RS: int, CS: int, RT: int, CT: int, S: List[str]):
    M = 10**10
    ws = ["#" * (W + 2)] + ["#" + row + "#" for row in S] + ["#" * (W + 2)]
    dxy = [(-1, 0), (0, +1), (+1, 0), (0, -1)]
    def calc(d: int) -> int:
        qs: List[List[int]] = [[M] * (W + 2) for _ in range(H + 2)]
        q: Deque[Tuple[int, int, int, int]] = deque()
        q.append((0, RS, CS, d))
        while q:
            l, y, x, d = q.popleft()
            if l >= qs[y][x]: continue
            qs[y][x] = l
            if y == RT and x == CT:
                return l
            y1, x1 = y + dxy[d][0], x + dxy[d][1]
            if ws[y1][x1] == "." and l < qs[y1][x1]:
                q.append((l, y1, x1, d))
            for dd in range(3):
                nd = (d + dd + 1) % 4
                y2, x2 = y + dxy[nd][0], x + dxy[nd][1]
                if ws[y2][x2] == "." and l + 1 < qs[y2][x2]:
                    q.append((l + 1, y2, x2, nd))
        # print(*qs, sep="\n", end="\n\n")
        return 0
    result = min(calc(0), calc(1), calc(2), calc(3))
    print(result)

def solve(H: int, W: int, RS: int, CS: int, RT: int, CT: int, S: List[str]):
    M = 10**10
    ws = ["#" * (W + 2)] + ["#" + row + "#" for row in S] + ["#" * (W + 2)]
    dxy = [(-1, 0), (0, +1), (+1, 0), (0, -1)]
    qs: List[List[List[int]]] = [[[M] * 4 for _ in range(W + 2)] for _ in range(H + 2)]
    q: Deque[Tuple[int, int, int, int]] = deque()
    q.append((0, RS, CS, 0))
    q.append((0, RS, CS, 1))
    q.append((0, RS, CS, 2))
    q.append((0, RS, CS, 3))
    while q:
        l, y, x, d = q.popleft()
        if l >= qs[y][x][d]: continue
        qs[y][x][d] = l
        y1, x1 = y + dxy[d][0], x + dxy[d][1]
        if ws[y1][x1] == "." and l < qs[y1][x1][d]:
            q.append((l, y1, x1, d))
        for dd in range(3):
            nd = (d + dd + 1) % 4
            y2, x2 = y + dxy[nd][0], x + dxy[nd][1]
            if ws[y2][x2] == "." and l + 1 < qs[y2][x2][nd]:
                q.append((l + 1, y2, x2, nd))
    #print(qs)
    #print(qs[RT][CT])
    result = min(qs[RT][CT])
    print(result)


solve(H, W, RS, CS, RT, CT, S)
