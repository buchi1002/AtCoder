from bisect import bisect

N = int(input())
As = list(map(int, input().split()))
S = set(As)
Aset = set(As)

Q = int(input())
Ss = [0]*(N+1)

Qs = list()
for _ in range(Q):
    l, r = map(int, input().split())
    if l not in S:
        As.append(l)
        S.add(l)

    if r not in S:
        As.append(r)
        S.add(r)

    Qs.append((l, r))

As.sort()
sleep = False
Ss = [0]*(len(As)+1)
v = 0
for idx in range(1,len(As)):
    if sleep:
        v += As[idx] - As[idx-1]

    if As[idx] in Aset:
        sleep = (not sleep)

    Ss[idx+1] = v


for l, r in Qs:
    l_idx = bisect(As, l)
    r_idx = bisect(As, r)
    print(Ss[r_idx] - Ss[l_idx])
