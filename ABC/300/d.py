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

def main():
    N = int(input())
    Ps = erato(3*(10**5))

    cnt = 0
    for ai in range(N):
        a = Ps[ai]
        if a**5 > N:
            break
        for bi in range(ai+1, N):
            b = Ps[bi]
            if b**3 > N:
                break
            for ci in range(bi+1, N):
                c = Ps[ci]
                if c**2 > N:
                    break
                if (a**2)*b*(c*c) > N:
                    break
                else:
                    cnt += 1

    print(cnt)

main()
