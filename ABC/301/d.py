def main():
    S = input().zfill(60)
    N = int(input())
    m = int(S.replace("?", "0"), 2)
    d = N - m
    if d < 0:
        print(-1)
    else:
        for i in range(60):
            if S[i] == "?":
                if (1 << (60 - i-1)) <= d:
                    d -= (1 << (60 - i-1))
        print(N-d)
main()
