from collections import defaultdict

def main():
    N, M = map(int,input().split())
    Xs = list(map(int,input().split()))
    B = defaultdict(lambda : 0)
    for i in range(M):
        C, Y = map(int,input().split())
        B[C] = Y
    dp = [[-1]*(N+2) for _ in range(N+2)]

    M = 0
    dp[0][0] = 0
    for i in range(1,N+1):
        dp[i][0] = M
        M = 0
        for j in range(1,N+1):
            dp[i][j] = dp[i-1][j-1] + Xs[i-1] + B[j]
            M = max(M,dp[i][j])

    print(dp)
if __name__ == '__main__':
    main()
