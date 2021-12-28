# https://atcoder.jp/contests/typical90/tasks/typical90_bf

from typing import Dict, List

N, K = [int(x) for x in input().split()]

def solve(N: int, K: int):
    n = N
    i = 0
    ts: Dict[int, int] = {n: 0}
    cs: List[int] = [n]
    while 1:
        n = (n + (n%10) + (n//10%10) + (n//100%10) + (n//1000%10) + (n//10000%10)) % 100000
        i += 1
        cs.append(n)
        if n in ts:
            break
        ts[n] = i

    if K <= ts[n]:
        print(cs[K])
    else:
        q = (K - ts[n]) % (i - ts[n]) + ts[n]
        print(cs[q])

solve(N, K)
