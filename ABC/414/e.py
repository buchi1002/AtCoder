MAX = 10 ** 6 + 10


L = [True] * (MAX + 1)
L[0] = L[1] = False
primes = list()
for i in range(2, MAX + 1):
    if i * i > MAX:
        for j in range(i, MAX + 1):
            if L[j]:
                primes.append(j)
        break
    else:
        if L[i]:
            primes.append(i)
            for j in range(2, MAX + 1):
                if i * j > MAX:
                    break
                L[i * j] = False

N = int(input())
MOD = 998244353

num_primes = (N - 1) # 2...N
for p in primes:
    if p > N:
        break
    num_primes -= (N//p - 1)


ans = ((N*N) - (N*(N-1)//2))
for p in primes:
    px = p
    while px <= N:
        ans = (ans - N//p)
        px *= p

if len(primes) < num_primes:
    ans = (ans - (num_primes - len(primes)))%MOD

print(ans%MOD)