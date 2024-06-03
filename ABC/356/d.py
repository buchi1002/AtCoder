def f(N, M):
    if N==0:
        return 0
    if N == 1:
        return M & 1
    else:
        k = len(bin(N)[2:])-1
        G = (1 << (k-1))*(bin(M&(1<<k) - 1)[2:].count("1"))
        R = ((M >> k)%2)*(N-(1<<k)+1)
        B = f(N-(1<<k), M)

        return (G+R+B)%998244353

N, M = map(int, input().split())
print(f(N, M))
