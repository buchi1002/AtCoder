from collections import deque

N = int(input())
Ps = tuple(map(int, input().split()))


c = N+10
idx = -1
L = deque()

for i in range(N-1, -1, -1):
    if Ps[i] <= c:
        c = Ps[i]
        idx = i
        L.appendleft(Ps[i])
    else:
        c = Ps[i]
        idx = i
        L.appendleft(Ps[i])

        break


M = -1
num = -1
v = -1
for i in range(len(L)-1, -1, -1):
    if L[i] < c:
        num = i
        v = L[i]

        break

L.remove(L[num])
L = list(L)
L.sort(key = lambda x: -x)

ans = list(Ps[:idx]) + [v] + L
print(*ans)
