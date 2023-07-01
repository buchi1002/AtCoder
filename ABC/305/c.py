H, W = map(int,input().split())
Ss = [input() for _ in range(H)]

l = W
r = 0
u = H
d = 0
for i in range(H):
    for j in range(W):
        if Ss[i][j] == "#":
            l = min(l, j)
            r = max(r, j)
            u = min(u, i)
            d = max(d, i)

for i in range(u, d+1):
    for j in range(l, r+1):
        if Ss[i][j] == ".":
            print(*[i+1, j+1])
