def prime(N:int, s:int = 2) -> list:
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
