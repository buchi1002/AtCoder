def main():
    D, G = map(int,input().split())
    Ps, Cs = list(), list()

    for i in range(D):
        p, c = map(int,input().split())
        Ps.append(p)
        Cs.append(c)

    NP = sum(Ps)
    dp = [[0]*(NP+1) for _ in range(D)]

    for j in range(1, Ps[0]):
        dp[0][j] = 100*j

    dp[0][Ps[0]] = 100*Ps[0] + Cs[0]

    for i in range(1,D):
        for j in range(NP+1):
            M = 0
            for p in range(Ps[i]):
                if j - p >= 0:
                    M = max(M, dp[i-1][j-p] + (i+1)*100*p)
            if j - Ps[i] >= 0:
                M = max(M, dp[i-1][j-Ps[i]] + (i+1)*100*Ps[i] + Cs[i])

            dp[i][j] = M

    for j in range(NP+1):
        if dp[D-1][j] >= G:
            print(j)
            break
main()
