def main():
    N = int(input())
    M = input()
    Q = int(input())

    S = [list(range(len(M)//2)), list(range(len(M)//2, len(M)))]
    dic = [0, 1]
    for i in range(Q):
        T, A, B = map(int, input().split())

        if T == 2:
            dic[0], dic[1] = dic[1], dic[0]

        else:
            if B <= N:
                S[dic[0]][A-1], S[dic[0]][B-1] = S[dic[0]][B-1], S[dic[0]][A-1]
            elif A <= N:
                S[dic[0]][A-1], S[dic[1]][B-1-N] = S[dic[1]][B-1-N], S[dic[0]][A-1]
            else:
                S[dic[1]][A-1-N], S[dic[1]][B-1-N] = S[dic[1]][B-1-N], S[dic[1]][A-1-N]

    s = ""
    for i in range(N):
        s += M[S[dic[0]][i]]
    for i in range(N):
        s += M[S[dic[1]][i]]

    print(s)







main()
