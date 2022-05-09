import math
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
def main():
    # input
    A, B, K = map(int, input().split())
    # compute
    N = 0
    n = A + B
    for i in range(A):
        c = comb(n, i)
        if K > c**c:
            N += 1
        else:
            break
        print(N)
        print(bin(int(bin(2**N -1)[2:]+bin(2**(B -N)-1)[2:]))[2:])


    # output

if __name__ == '__main__':
    main()
