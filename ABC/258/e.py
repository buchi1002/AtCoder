def main():
    N, Q, X = map(int,input().split())
    Ws = list(map(int,input().split()))

    S = set()
    idx = 0
    L = []
    D = {}
    num = 0

    while idx not in S:
        S.add(idx)
        D[idx] = num
        w = 0
        count = 0
        while w < X:
            count += 1
            w += Ws[idx]
            idx = (idx+1)%N
        L.append(count)
        num += 1

    f = D[idx]
    cy = num - f

    for i in range(Q):
        K = int(input())
        if K <= len(L):
            print(L[K-1])
        else:
            K = K - 1
            K = (K - f)%cy
            print(L[f + K])

if __name__ == '__main__':
    main()
