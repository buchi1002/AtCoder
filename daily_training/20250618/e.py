from collections import defaultdict
from atcoder.segtree import SegTree
# class SegTree:
#     """
#     init(init_val, ide_ele): 配列init_valで初期化 O(N)
#     update(k, x): k番目の値をxに更新 O(logN)
#     query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
#     """
#     def __init__(self, init_val, segfunc, ide_ele):
#         """
#         init_val: 配列の初期値
#         segfunc: 区間にしたい操作
#         ide_ele: 単位元
#         n: 要素数
#         num: n以上の最小の2のべき乗
#         tree: セグメント木(1-index)
#         """
#         n = len(init_val)
#         self.segfunc = segfunc
#         self.ide_ele = ide_ele
#         self.num = 1 << (n - 1).bit_length()
#         self.tree = [ide_ele] * 2 * self.num
#         # 配列の値を葉にセット
#         for i in range(n):
#             self.tree[self.num + i] = init_val[i]
#         # 構築していく
#         for i in range(self.num - 1, 0, -1):
#             self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])
    
#     def update(self, k, x):
#         """
#         k番目の値をxに更新
#         k: index(0-index)
#         x: update value
#         """
#         k += self.num
#         self.tree[k] = x
#         while k > 1:
#             self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
#             k >>= 1

#     def query(self, l, r):
#         """
#         [l, r)のsegfuncしたものを得る
#         l: index(0-index)
#         r: index(0-index)
#         """
#         res = self.ide_ele

#         l += self.num
#         r += self.num
#         while l < r:
#             if l & 1:
#                 res = self.segfunc(res, self.tree[l])
#                 l += 1
#             if r & 1:
#                 res = self.segfunc(res, self.tree[r - 1])
#             l >>= 1
#             r >>= 1
#         return res


Q = int(input())
qs = [list(map(int, input().split())) for _ in range(Q)]


s = set()
for q in qs:
    if q[0] == 1:
        x = q[1]
        s.add(x)
d = {v: i for i, v in enumerate(sorted(s))}
dr = {i: v for i, v in enumerate(sorted(s))}


stmaxi = SegTree(max, 0, [0]*(Q+1))
stmini = SegTree(min, 10**8, [10**8]*(Q+1))

num = defaultdict(lambda : 0)
for q in qs:
    if q[0] == 1:
        _, x = q
        stmaxi.set(d[x], d[x])
        stmini.set(d[x], d[x])
        num[d[x]] += 1
    elif q[0] == 2:
        _, x, c = q
        if x not in d:
            continue
        m = min(c, num[d[x]])
        if num[d[x]] <= c:
            stmini.set(d[x], 10**8)
            stmaxi.set(d[x], 0)
        num[d[x]] -= m
    else:
        print(dr[stmaxi.all_prod()] - dr[stmini.all_prod()])