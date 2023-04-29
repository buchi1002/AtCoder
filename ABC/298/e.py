def main():
    mod = 998244353
    N, A, B, P, Q = map(int, input().split())
    iP = pow(P, -1, mod)
    iQ = pow(Q, -1, mod)
    dp = [[0]*N for _ in range(N)]

    dp[A-1][B-1] = 1
    for i in range(A-1, N-1):
        for j in range(B-1, N-1):
            for p in range(1, P+1):
                for q in range(1, Q+1):
                    dp[min(i+p, N-1)][min(j+q, N-1)] = (dp[min(i+p, N-1)][min(j+q, N-1)] + dp[i][j]*iP*iQ)%mod

    ans = 0
    for i in range(N):
        ans = (ans + dp[-1][i])%mod

    print(ans)
main()
