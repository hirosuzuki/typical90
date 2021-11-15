# https://atcoder.jp/contests/typical90/tasks/typical90_c

from typing import List, DefaultDict, Set, Tuple, Deque, Dict
from collections import defaultdict, deque

N = int(input())
AB = [[int(_) for _ in input().split()] for _ in range(N - 1)]


def solve(N: int, AB: List[List[int]]):
    ds: DefaultDict[int, Set[int]] = defaultdict(set)
    for a, b in AB:
        ds[a].add(b)
        ds[b].add(a)

    def calc_longest(start: int) -> Tuple[int, int]:
        distance: Dict[int, int] = {}
        q: Deque[Tuple[int, int]] = deque()
        q.append((start, 0))
        while q:
            i, d = q.popleft()
            if i not in distance:
                distance[i] = d
            for n in ds[i]:
                if n not in distance:
                    q.append((n, d + 1))
        return (i, d)

    p1, _ = calc_longest(1)
    _, l = calc_longest(p1)

    print(l + 1)


solve(N, AB)
