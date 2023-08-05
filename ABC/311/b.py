N, D = map(int, input().split())

Ss = [input() for _ in range(N)]


c = 0
Mc = 0
for d in range(D):
    c += 1
    for i in range(N):
        if Ss[i][d] == "x":
            c = 0
    Mc = max(Mc, c)


print(Mc)
