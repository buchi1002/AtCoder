# （参考）https://note.nkmk.me/python-union-find/

import sys
from collections import defaultdict
sys.setrecursionlimit(100000000)

class UnionFind():
    def __init__(self):
        self.parents = defaultdict(lambda:-1)

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def add(self, x):
        self.parents[x]

    # x のグループに y のグループを追加
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def roots(self):
        return [key  for key, value in enumerate(self.parents) if value < 0]

    def n(self):
        return len(self.parents.keys())

    def size(self, x):
        return -self.parents[self.find(x)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n()) if self.find(i) == root]

    def all_group_members(self):
        group_members = defaultdict(list)
        for x in self.parents.keys():
            group_members[self.find(x)].append(x)

        return group_members
