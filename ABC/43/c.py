from collections import defaultdict
def culc(z,SA,SA2,N):
    return SA2 - 2*z*SA + N*(z**2)

def main():
    N = int(input())
    As = list(map(int, input().split()))

    SA = sum(As)

    SA2 = 0
    for i in range(N):
        SA2 += As[i]**2

    Ans1 = SA//N
    Ans2 = Ans1 + 1

    Ans1 = culc(Ans1,SA,SA2,N)
    Ans2 = culc(Ans2,SA,SA2,N)

    print(min(Ans1,Ans2))

if __name__ == '__main__':
    main()
