def main():
    N, K, Q = map(int,input().split())
    As = list(map(int,input().split()))
    Ls = list(map(int,input().split()))

    M = [0]*(N+1)
    Mdic = {}
    for k in range(K):
        M[As[k]] = 1
        Mdic[k] = As[k]

    for q in range(Q):
        if Mdic[Ls[q]-1] != N and M[Mdic[Ls[q]-1]+1] != 1:
            M[Mdic[Ls[q]-1]] = 0
            M[Mdic[Ls[q]-1]+1] = 1
            Mdic[Ls[q]-1] += 1
    Ans = []
    for i in range(K):
        Ans.append(Mdic[i])
    print(*Ans)

if __name__ == '__main__':
    main()
