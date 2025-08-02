N, Q = map(int, input().split())
Xs = [x-1 for x in list(map(int, input().split()))]
Bs = [0] * N
ans = [0] * Q
for x in range(Q):
    if Xs[x] == -1:
        Mini = -1
        Min = 101
        for i in range(N):
            if Bs[i] < Min:
                Mini = i
                Min = Bs[i]
        Bs[Mini] += 1
        ans[x] = Mini + 1
    else:
        Bs[Xs[x]] += 1
        ans[x] = Xs[x] + 1
print(*ans)