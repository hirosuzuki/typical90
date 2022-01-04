# https://atcoder.jp/contests/typical90/tasks/typical90_bt

from typing import List

H, W = [int(x) for x in input().split()]
C = [input() for _ in range(H)]

def solve(H: int, W: int, C: List[str]):
    result = 0
    def start(startx: int, starty: int):
        def check(sx: int, sy: int, cs: List[bool], l: int):
            nonlocal result
            cs = cs[:]
            cs[sy * W + sx] = True
            for dy, dx in (-1, 0), (+1, 0), (0, -1), (0, +1):
                x, y = sx + dx, sy + dy
                if x == startx and y == starty:
                    result = max(result, l + 1)
                if 0 <= x < W and 0 <= y < H and C[y][x] == "." and cs[y * W + x] is False:
                    check(x, y, cs, l + 1)
        check(x, y, [False] * (W * H), 0)
    for y in range(H):
        for x in range(W):
            if C[y][x] == ".":
                start(x, y)
    if result < 3:
        result = -1
    print(result)


solve(H, W, C)
