# https://atcoder.jp/contests/typical90/tasks/typical90_w

from typing import List, Tuple

H, W = [int(x) for x in input().split()]
C = [input() for _ in range(H)]


def solve(H: int, W: int, C: List[str]):
    if H > 4 or W > 4:
        return

    result = 0
    for i in range(2 ** (H * W)):
        p: List[Tuple[int, int]] = []
        for y in range(H):
            for x in range(W):
                j = y * W + x
                if i & (1 << j):
                    p.append((x, y))
        if any(C[y][x] == "#" for x, y in p):
            continue
        if any(p[j][0] - 1 <= p[i][0] <= p[j][0] + 1 and
               p[j][1] - 1 <= p[i][1] <= p[j][1] + 1
               for i in range(len(p))
               for j in range(i + 1, len(p))):
            continue
        result += 1

    print(result)


solve(H, W, C)
