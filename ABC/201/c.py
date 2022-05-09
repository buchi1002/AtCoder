import math
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
def main():
    # input
    S = input()
    # compute
    o = S.count("o")
    q = S.count("?")
    # output
    if o == 4:
        print(int(math.factorial(4)))
    elif o == 3:
        print(int(math.factorial(4)*(q +3/2)))
    elif o == 2:
        if q >= 2:
            print(int(2**4 - 2 + (math.factorial(4)*q) + math.factorial(4)*comb(q, 2) + math.factorial(4)*q/2))
        else:
            print(int(2**4 - 2 + (math.factorial(4)*q) +  math.factorial(4)*q/2))
    elif o == 1:
        print(int(4*(q**3) + comb(4, 2)*q*q + 4*q + 1))
    elif o == 0:
        print(int(q**4))
    else:
        print(int(0))

if __name__ == '__main__':
    main()
