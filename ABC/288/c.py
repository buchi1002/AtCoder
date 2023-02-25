from  collections import defaultdict
import sys

sys.setrecursionlimit(1000000)

def rec(key):
    if key in S:
        return
    else:
        S.add(key)
        C.add(key)

    for k in G[key]:
        rec(k)

    return

N, M = map(int,input().split())

G = defaultdict(lambda:list())

for i in range(M):
    a, b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

Cs = list()
S = set()
for i in range(1,N+1):
    if i not in S:
        Cs.append(set())
        C = Cs[-1]
        rec(i)

count = 0
for C in Cs:
    n_v = len(C)
    n_e = 0
    for v in C:
        n_e += len(G[v])
    n_e = n_e//2

    count += n_e - n_v + 1

print(count)
