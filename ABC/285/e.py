def main():
    N = int(input())

    As = tuple(map(int,input().split()))
    chain = [0]
    s = 0
    for i in range(1,N):
        if i%2 != 0:
            v = As[i//2]
        else:
            v = As[i//2 - 1]

        s += v
        chain.append(s)

    dp = [[0]*N for i in range(N)]
    dp = [0]*(N+1)
    dp[3] = chain[1]
    dp[4] = chain[2]
    for i in range(N):
        for j in range(N):


    for i in range(N):
        dp[i][1] = chain[N-1]

    for i in range(N):
        for j in range(N)

main()
