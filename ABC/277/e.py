from collections import defaultdict

N, M, K = map(int, input().split())
d = defaultdict(lambda:set())
for i in range(M):
    u, v, a = map(int, input().split())
    if a:
        d[u].add(v)
        d[v].add(u)
    else:
        d[-u].add(-v)
        d[-v].add(-u)

Bs = list(map(int, input().split()))
B = set()
for i in range(len(Bs)):
    B.add(Bs[i])
    B.add(-Bs[i])

C = set()
S = set()
S.add(1)
C |= d[1]
if -1 in B:
    C |= d[-1]
    S.add(-1)

flag = False
switch = 1
count = 0
while len(C) != 0:
    S |= C
    count += 1
    if (N in C) or (-N in C):
        flag = True
        break
    L = set()
    for key in C:
        L |= d[key]
        if key in B:
            L |= d[-key]

    C = L - S

if flag:
    print(count)
else:
    print(-1)
