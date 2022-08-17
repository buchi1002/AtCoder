from collections import defaultdict
def main():
    N = int(input())
    As = list(map(int, input().split()))
    if N == 1:
        print(0)
    else:
        D = defaultdict(lambda : 0)
        for i in range(N):
                D[i] += 1

        L = [0]*(N+1)
        S = N
        for i in range(N+1):
            S -= D[i]
            L[N-i] = S

        s = 0
        while s != N-1:
            As[s]

if __name__ == '__main__':
    main()
