# https://atcoder.jp/contests/typical90/tasks/typical90_z

from typing import List, DefaultDict, Set, Deque, Tuple
from collections import defaultdict, deque

N = int(input())
AB = [[int(x) for x in input().split()] for _ in range(N - 1)]


def solve(N: int, AB: List[List[int]]):

    ds: DefaultDict[int, Set] = defaultdict(set)

    for a, b in AB:
        ds[a].add(b)
        ds[b].add(a)

    ls: List[int] = [0] * (N + 1)

    q: Deque[Tuple[int, int]] = deque()

    q.append((1, 1))
    while q:
        n, l = q.popleft()
        if ls[n] > 0:
            continue
        ls[n] = l
        for m in ds[n]:
            if ls[m] == 0:
                q.append((m, l + 1))

    odd_list = [i for i in range(1, N + 1) if ls[i] % 2 == 1]
    even_list = [i for i in range(1, N + 1) if ls[i] % 2 == 0]

    if len(odd_list) >= N // 2:
        result = odd_list[:N // 2]
    else:
        result = even_list[:N // 2]

    print(*result)


solve(N, AB)
