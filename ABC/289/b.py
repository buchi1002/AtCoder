from collections import deque

N, M = map(int,input().split())
As = set(map(int,input().split()))

que = list()
Ps = list()
for i in range(1, N+1):
    if i in As:
        que.append(i)
    else:
        Ps.append(i)
        l = len(que)
        for q in range(len(que)-1, -1, -1):
            Ps.append(que[-1])
            que.pop()


print(*Ps)
