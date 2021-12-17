# https://atcoder.jp/contests/typical90/tasks/typical90_ak

from typing import List

W, N = [int(x) for x in input().split()]
LRV = [[int(x) for x in input().split()] for _ in range(N)]


# https://qiita.com/takayg1/items/c811bd07c21923d7ec69
class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

def solve(W: int, N: int, LRV: List[List[int]]):
    L = -10**20
    xs = [L] * (W + 1)
    xs[0] = 0
    for l, r, v in LRV:
        sg = SegTree(xs, max, L)
        nxs = [L] * (W + 1)
        for i in range(W + 1):
            v1 = xs[i]
            if i - l >= 0:
                v2 = sg.query(max(i - r, 0), i - l + 1) + v
            else:
                v2 = L
            nxs[i] = max(v1, v2)
        xs = nxs
        # print(xs, "\n\n")
        # break

    if xs[-1] >= 0:
        print(xs[-1])
    else:
        print(-1)


solve(W, N, LRV)
