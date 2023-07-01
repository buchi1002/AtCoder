mod = 998244353

from collections import defaultdict

def make_comb(n):
    comb = [[1]+[0]*n for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1, n+1):
            comb[i][j] = comb[i-1][j-1] + comb[i-1][j]

    return comb
def get_yaku(n):
    Ms = list()
    for i in range(1, n):
        if i*i >= n:
            break

        if N%i == 0:
            Ms.append(i)

    return Ms

N = int(input())
S = int(input().replace("#", "0").replace(".", "1"))

Ms = get_yaku(N)
d = defaultdict(lambda:list())
for M in Ms:
    d[M] = get_yaku(M)

comb = make_comb(Ms[-1])

cnt = 0
LM = [0]*len(Ms)
for i in range(len(Ms)):
    M = Ms[i]
    C = 0
    V = S
    K = N//M
    for k in range(K):
        C |= (V%(1<<M))
        V //(1<<M)
    nbit = format(C, "b").count("1")
    LM = pow(2, N-nbit, mod)

cnt = 0
for i in range(len(M))
