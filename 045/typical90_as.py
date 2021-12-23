# https://atcoder.jp/contests/typical90/tasks/typical90_as

from typing import List, Tuple, Dict

N, K = [int(x) for x in input().split()]
XY = [[int(x) for x in input().split()] for _ in range(N)]


def solve1(N: int, K: int, XY: List[List[int]]):
    BE = Tuple[int, ...]
    vs: List[BE] = [tuple(k for k in range(N) if (1 << k) & i)
                    for i in range(2**N)]
    # print(vs)

    d: Dict[BE, int] = {}
    for v in vs:
        if len(v) >= 2:
            n = v[-1]
            r = d[v[:-1]]
            for i in v[:-1]:
                l = (XY[n][0] - XY[i][0]) ** 2 + (XY[n][1] - XY[i][1]) ** 2
                r = max(r, l)
            d[v] = r
        else:
            d[v] = 0
    # print(d)

    dp: Dict[Tuple[BE, int], int] = {}
    for v in vs:
        dp[v, 0] = 0
    for v in vs:
        dp[v, 1] = d[v]
    for i in range(2, K + 1):
        for v in vs:
            rr = 10**30
            svs = [tuple(v[x] for x in s) for s in vs[:1 << len(v)]]
            for w in svs:
                nv = tuple(x for x in v if x not in w)
                r = max(dp[w, i - 1], d[nv])
                #print(i, v, w, nv, r, dp[w, i - 1], d[nv])
                rr = min(rr, r)
            dp[v, i] = rr

    # print(dp)

    print(dp[vs[-1], K])


def solve(N: int, K: int, XY: List[List[int]]):

    d: List[int] = [0] * (2**N)
    for i in range(2**N):
        n = i.bit_length() - 1
        if n >= 1:
            c = i ^ (1 << n)
            r = d[c]
            xs = [(XY[n][0] - XY[j][0])**2 + (XY[n][1] - XY[j][1])**2
                  for j in range(n) if (1 << j) & i]
            if xs:
                r = max(r, max(xs))
            d[i] = r

    # print(d)

    dp: List[List[int]] = [[0] * (2**N) for _ in range(K + 1)]
    for i in range(2**N):
        dp[1][i] = d[i]
    for k in range(2, K + 1):
        for i in range(2**N):
            r = 10**30
            j = i
            while True:
                x = max(dp[k - 1][j], d[i - j])
                r = min(r, x)
                if j == 0:
                    break
                j = (j - 1) & i
            dp[k][i] = r
    print(dp[-1][-1])


solve(N, K, XY)
