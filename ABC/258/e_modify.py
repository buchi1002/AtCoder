def main():
    N, Q, X = map(int,input().split())
    Ws = list(map(int,input().split()))


    W = sum(Ws)

    X = X%W
    S = (X//W)*W
    count = (X//W)*N

    start = 0
    end = 0
    D = {}
    while start < N:
        if S < X:
            S += Ws[end]
            count += 1
            end = (end + 1)%N
        else:
            D[start] = [count,end]
            S -= Ws[start]
            start += 1
            count -= 1
            if start > end:
                end = start

    idx = 0
    D2 = [0]*N
    D3 = {}
    num = 0
    for i in range(N):
        D2[i] = (D[idx][0])
        D3[idx] = num
        num += 1
        idx = D[idx][1]

        if idx in D3:
            break

    ficnt = D3[idx]
    cycnt = num - ficnt

    for _ in range(Q):
        K = int(input()) - 1
        if K < num:
            print(D2[K])
        else:
            K = ficnt + (K - ficnt)%cycnt
            print(D2[K])

if __name__ == '__main__':
    main()
