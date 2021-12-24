# https://atcoder.jp/contests/typical90/tasks/typical90_at

from typing import List

N = int(input())
ABC = [[int(x) for x in input().split()] for _ in range(3)]

def solve(N: int, ABC: List[List[int]]):
    cs: List[List[int]] = [[0] * 46 for _ in range(3)]
    for i in range(3):
        for x in ABC[i]:
            cs[i][x % 46] += 1
    result = 0
    for a in range(46):
        for b in range(46):
            c = (46 - a - b) % 46
            r = cs[0][a] * cs[1][b] * cs[2][c]
            result += r
            #if cs[0][a] | cs[1][b] | cs[2][c]:
            #    print(a, b, c, cs[0][a], cs[1][b], cs[2][c], r, result)
    #print(*cs, sep="\n")
    print(result)


solve(N, ABC)
