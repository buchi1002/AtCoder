def main():
    N = int(input())
    S = input()
    start = 0
    end = 0
    M = -1
    c = -1

    cnt = 0
    M = -1
    for i in range(N):
        if S[i] == "-":
            cnt = 0
        elif S[i] == "o":
            cnt += 1
            M = max(M, cnt)

    if S.count("-") == 0:
        print(-1)
    else:
        print(M)


main()
