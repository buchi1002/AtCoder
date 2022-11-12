N, M = map(int, input().split())
As = list(map(int, input().split()))
As.sort()

L = [[]]
v = (As[0]%M)
L[0].append(v)
idx = 0
for i in range(1, N):
    if (As[i] == v) or (As[i] == (v+1)):
        L[idx].append(As[i])
        v = As[i]
    else:
        L.append([])
        idx += 1
        L[idx].append(As[i])
        v = As[i]


if len(L)>=2 and L[-1][-1] == M-1 and L[0][0] == 0:
    L[0] += L[-1]

K = sum(As)
ans = K
for i in range(len(L)):
    ans = min(K - sum(L[i]), ans)

print(ans)
