from collections import defaultdict

def rec(key):
    if key in S:
        return

    S.add(key)

    for k in d[key]:
        rec(k)

    return

N, M = map(int,input().split())
d = defaultdict(lambda:set())

for _ in range(M):
    u,v = map(int,input().split())
    d[u].add(v)
    d[v].add(u)

S = set()
count = 0
for p in range(1,N+1):
    if p not in S:
        count += 1
        rec(p)

print(count)
