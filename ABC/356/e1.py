from math import floor
N = int(input())
As = list(map(int, input().split()))

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        ans += floor(max(As[i], As[j])/min(As[i], As[j]))
print(ans)
