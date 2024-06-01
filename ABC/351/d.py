import sys
sys.setrecursionlimit(100000000)

def connect(y,x,H,W):
    L = list()
    if y - 1 >= 0:
        L.append((y-1,x))
    if x - 1 >= 0:
        L.append((y,x-1))
    if x + 1 < W:
        L.append((y,x+1))
    if y + 1 < H:
        L.append((y+1,x))
    return L

def rec(key, M, s):
    if key in s:
        return
    s.add(key)
    C = connect(key[0], key[1], len(M), len(M[0]))
    if all(M[c[0]][c[1]] == "." for c in C):
        for k in C:
            rec(k, M, s)
    return

H, W = map(int, input().split())
M = [[x for x in input()] for _ in range(H)]

seen = set()
m = 1
for i in range(H):
    for j in range(W):
        if not (i, j) in seen and M[i][j] != "#":
            s = set()
            rec((i, j), M, s)
            m = max(len(s), m)
            seen |= s

print(m)
