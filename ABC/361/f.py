from math import sqrt, floor, gcd, prod, pow as Pow
def erato(N:int, s:int = 2) -> list:
    p_judge = [True]*(N+1)
    p_judge[0:min(N, 2)] = [False]*min(N, 2)
    primes = list()
    for i in range(s, N+1):
        if p_judge[i]:
            primes.append(i)
            for j in range(2, N+1):
                if i*j > N:
                    break
                p_judge[i*j] = False
    return primes

def r_exp(x):
    primes = erato(10**6)
    exps = list()
    for p in primes:
        exp = 0
        while True:
            x_n, x_r = divmod(x, p)
            if x_r !=0 :
                break
            exp += 1
            x = x_n
        if exp:
            exps.append(exp)
    if len(exps) == 0:
        exps.append(1)

    return exps

def main():
    N = int(input())
    s = set()
    for i in range(2, (10**6)+1):
        print(i)
        for j in range(2, 60):
            x = pow(i, j)
            if pow(i, j) <= N:
                s.add(x)

    print(len(s))
main()
