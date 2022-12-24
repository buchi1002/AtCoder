import itertools
def main():
    N, K, D = map(int,input().split())
    As = tuple(map(int,input().split()))

    dp = [[[-1]*D for i in range(K+1)] for j in range(N)]

    dp[0][1][As[0]%D] = As[0]
    dp[0][0][0] = 0

    for i in range(1,N):
        dp[i][0][0] = 0
        for j in range(1,K+1):
            for k in range(D):
                if dp[i-1][j-1][(k-As[i])%D] != -1:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-1][(k-As[i])%D] + As[i])
                else:
                    dp[i][j][k] = dp[i-1][j][k]
    print(dp[N-1][K][0])

main()
