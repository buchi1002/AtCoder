def main():
    N, M = map(int,input().split())
    mod = 998244353
    As = [0]*(N+3)
    As[2] = (M*(M-1))%mod
    As[3] = (M*(M-1)*(M-2))%mod
    for i in range(4, N+1):
        As[i] = ((As[i-1]*(M-2) + As[i-2]*(M-1)))%mod

    print(As[N])
main()
