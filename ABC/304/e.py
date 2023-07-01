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


def main():
    N, M = map(int, input().split())

    union = UnionFind(N)
    for _ in range(M):
        u,v = map(int,input().split())
        union.union(u-1, v-1)

    K = int(input())
    taboo = set()
    for _ in range(K):
        x, y = map(int, input().split())
        xp = union.find(x-1)
        yp = union.find(y-1)

        taboo.add((xp, yp))
        taboo.add((yp, xp))

    Q = int(input())
    for _ in range(Q):
        p, q = map(int, input().split())
        pp = union.find(p-1)
        qp = union.find(q-1)
        flag = (pp, qp) not in taboo
        if flag:
            print("Yes")
        else:
            print("No")
main()
