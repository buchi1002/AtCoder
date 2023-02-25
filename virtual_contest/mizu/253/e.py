from collections import defaultdict
def main():
    p = 998244353
    N, M, K = map(int, input().split())
    rM = pow(M, p-2, p)%p

    Ps = [[0]*(N+1) for i in range(K+1)]
    Ps[0][0] = 1
    for k in range(K):
        for i in range(N+1):
            if i == N:
                Ps[k+1][N] = (Ps[k+1][N] +Ps[k][N])%p
                continue
            for m in range(1,M+1):
                if i+m <= N:
                    Ps[k+1][i+m] = (Ps[k+1][i+m] + (Ps[k][i]*rM)%p)%p
                else:
                    Ps[k+1][2*N-i-m] = (Ps[k+1][2*N-i-m] + (Ps[k][i]*rM)%p)%p

    print(Ps[K][N])


if __name__ == '__main__':
    main()
