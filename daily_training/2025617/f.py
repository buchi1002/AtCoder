N = int(input())
Hs = list(map(int, input().split()))
M = 1
for s in range(N):
    for x in range(N):
        for i in range(N+1):
            if (s + x * i >= N) or (Hs[s + x * i] != Hs[s]):
                M = max(i, M)
                break

print(M)