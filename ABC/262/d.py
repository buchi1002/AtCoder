def main():
    N = int(input())
    As = map(int,input().split())

    dp = [[[0,0] for j in range(N+1)] for i in range(N)]

    for i in range(N):
        for j in range(N+1):
            if j <= i+1:
                dp[i][j] = dp[i][j]


if __name__ == '__main__':
    main()
