from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

def connect(y,x,H,W):
    L = list()
    if y - 1 >= 0:
        L.append((y-1,x))
    if x - 1 >= 0:
        L.append((y,x-1))
    if x + 1 < W:
        L.append((y,x+1))
    if y + 1 < H:
        L.append((y+1,x))
    return L

mod = 998244353
H, W = map(int, input().split())
G = [input() for _ in range(H)]
uf = UnionFind(10000000)
for i in range(H):
    for j in range(W):
        if G[i][j] == "#":
            for y, x in connect(i, j, H, W):
                if G[y][x] == "#":
                    uf.union(i*100000+j, y*1000000+x)

nR = 0
for i in range(H):
    for j in range(W):
        if G[i][j] == ".":
            nR += 1
ans = 0
for i in range(H):
    for j in range(W):
        if G[i][j] == ".":
            s = set()
            for y, x in connect(i, j, H, W):
                s +=
