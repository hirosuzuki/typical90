# https://atcoder.jp/contests/typical90/tasks/typical90_ac

from typing import List

W, N = [int(x) for x in input().split()]
LR = [[int(x) for x in input().split()] for _ in range(N)]

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


def solve(W: int, N: int, LR: List[List[int]]):

    LV = ((W+2)-1).bit_length()
    N0 = 2**LV
    data = [0]*(2*N0)
    lazy = [None]*(2*N0)

    # 伝搬対象の区間を求める
    def gindex(l, r):
        L = (l + N0) >> 1
        R = (r + N0) >> 1
        lc = 0 if l & 1 else (L & -L).bit_length()
        rc = 0 if r & 1 else (R & -R).bit_length()
        for i in range(LV):
            if rc <= i:
                yield R
            if L < R and lc <= i:
                yield L
            L >>= 1
            R >>= 1

    # 遅延伝搬処理
    def propagates(*ids):
        for i in reversed(ids):
            v = lazy[i-1]
            if v is None:
                continue
            lazy[2*i-1] = data[2*i-1] = lazy[2*i] = data[2*i] = v
            lazy[i-1] = None

    # 区間[l, r)をxで更新
    def update(l, r, x):
        *ids, = gindex(l, r)
        propagates(*ids)

        L = N0 + l
        R = N0 + r
        while L < R:
            if R & 1:
                R -= 1
                lazy[R-1] = data[R-1] = x
            if L & 1:
                lazy[L-1] = data[L-1] = x
                L += 1
            L >>= 1
            R >>= 1
        for i in ids:
            data[i-1] = max(data[2*i-1], data[2*i])

    # 区間[l, r)内の最大値を求める
    def query(l, r):
        propagates(*gindex(l, r))
        L = N0 + l
        R = N0 + r

        s = 0
        while L < R:
            if R & 1:
                R -= 1
                s = max(s, data[R-1])
            if L & 1:
                s = max(s, data[L-1])
                L += 1
            L >>= 1
            R >>= 1
        return s

    for l, r in LR:
        x = query(l, r + 1)
        update(l, r + 1, x + 1)
        print(x + 1)


solve(W, N, LR)
