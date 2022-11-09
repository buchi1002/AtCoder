def connect(t):
    y, x = t
    L = set()
    if ((y-1,x) not in S) and grid[y-1][x] == ".":
        L.add((y-1, x))

    if ((y, x-1) not in S) and grid[y][x-1] == ".":
        L.add((y, x-1))

    if ((y, x+1) not in S) and grid[y][x+1] == ".":
        L.add((y, x+1))

    if ((y+1, x) not in S) and grid[y+1][x] == ".":
        L.add((y+1, x))

    return L

H, W = map(int, input().split())
grid = ["#"*(W+2)]
for i in range(H):
    col = "#" + input() + "#"
    grid.append(col)
grid.append("#"*(W+2))

for j in range(H+2):
    for i in range(W+2):
        if grid[j][i] == "S":
            start = (j, i)

sy, sx = start
Goals = [(sy-1, sx), (sy, sx-1), (sy, sx+1), (sy+1, sx)]
S = set()
flag = False
for g in Goals:
    G = set(Goals)
    G.discard(g)
    S = set()

    search = connect(g)
    S |= search

    L = set()
    while len(search) != 0:
        L = set()
        for loc in search:
            L |= connect(loc)
        search = L.copy()
        S |= search
    if len(S & G) != 0:
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")
