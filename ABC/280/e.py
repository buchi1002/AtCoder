from collections import defaultdict

def main():
    mod = 998244353

    N, P = map(int,input().split())
    p_c = (P*pow(100,-1,mod))%mod
    p_n = (1-P)%mod

    dp = [0]*(N+10)
    dp[0] = 0
    for i in range(1,N+1):
        dp[i] = ((dp[max(0, i-2)] * p_c + dp[i-1] * p_n) + 1)%mod

    print(dp[N])

main()
