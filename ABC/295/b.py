R, C = map(int, input().split())
Bs = [[True]*C for _ in range(R)]

Bombs = list()
for i in range(R):
    S = input()
    for j in range(C):
        if S[j] == "#":
            Bs[i][j] = False
        if S[j] in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
            Bombs.append([i, j, int(S[j])])

for y, x, impact in Bombs:
    for i in range(R):
        for j in range(C):
            if abs(i - y) + abs(j - x) <= impact:
                Bs[i][j] = True

for i in range(R):
    print("".join(list(map(lambda flag: "." if flag else "#", Bs[i]))))
