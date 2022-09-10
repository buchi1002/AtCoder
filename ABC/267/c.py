def main():
    N, M = map(int,input().split())
    As = list(map(int,input().split()))

    d = sum(As[:M])
    V = sum([As[i]*(i+1) for i in range(M)])
    Max = V
    idx_s = 0
    idx_e = M
    while idx_e < N:
        V = V -d + As[idx_e]*M
        d = d - As[idx_s] + As[idx_e]

        Max = max(V, Max)
        idx_e += 1
        idx_s += 1

    print(Max)
if __name__ == '__main__':
    main()
