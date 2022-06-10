import math

def main():
    N, A, B = map(int, input().split())
    S = N*(N+1)//2

    NA = N//A
    SA = A*NA*(NA+1)//2

    NB = N//B
    SB = B*NB*(NB+1)//2

    lAB = A*B//math.gcd(A,B)
    NAB = N//lAB
    SAB = lAB*NAB*(NAB+1)//2

    print(S - SA - SB + SAB)
if __name__ == '__main__':
    main()
