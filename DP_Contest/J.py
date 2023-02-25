N = int(input())
a = list(map(int, input().split()))

dp = [[[0]*a[i] for i in range(3*N+1)] for _ in range(N+1)]

for i in range(1, N):
    for j in range(3*N+1):
        for k in range(3):
            dp[i][j][k] =
