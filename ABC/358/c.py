def main():
    N, M = map(int, input().split())
    S = list()
    m = 20
    for _ in range(N):
        s = input()
        s = s.replace("o", "1").replace("x", "0")
        S.append(int(s, 2))

    for bi in range(1<<N):
        check = 0
        cnt = 0
        for i, b in enumerate(reversed(bin(bi)[2:].zfill(N))):
            if b=="1":
                check |= S[i]
                cnt += 1

        if check == ((1<<M) - 1):
          m = min(m, cnt)

    print(m)
main()
