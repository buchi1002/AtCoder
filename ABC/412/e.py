MAX = 10**7 + 1
def main():
    
    B = [True]*MAX
    B[0] = False
    B[1] = False
    primes = list()
    for i in range(2, MAX):
        if i*i > MAX:
            break
        if B[i]:
            primes.append(i)
            for j in range(2, MAX):
                if i * j < MAX:
                    B[i * j] = False
                else:
                    break

    L, R = map(int, input().split())
    LRprimes = [True] * (R - L + 1)
    for p in primes:
        for j in range(max(2, L//p), R//p + 1):
            if L <= p*j <= R:
                LRprimes[p*j - L] = False

    for p in primes:
        pi = p
        if pi > R:
            break
        while pi <= R:
            if L <= pi:
                LRprimes[pi - L] = True
            pi *= p

    LRprimes[0] = 1

    print(sum(x for x in LRprimes))

        
main()