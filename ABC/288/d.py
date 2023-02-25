def main():

    N, K = map(int,input().split())
    As = list(map)
    Q = int(input())

    d = [list() for i in range(N)]
    Res = [0]*N

    l = 0
    r = K-1
    idx = 0
    ignore = 0
    while l <= N-K and r <= N-K:
        if idx - K + 1>= 0:
            ignore  -= Res[idx - K + 1]

        if ignore != As[idx]:
            Res[idx] = As[idx] - ignore
            ignore = As[idx]
        else:
            d[l].append(r)
            ignore = As[idx]
            r += 1

        idx += 1

        if idx > r:

main()
