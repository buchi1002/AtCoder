from collections import defaultdict
def main():
    H, W = map(int,input().split())
    Ss = list()
    for _ in range(H):
        Ss.append(input())

    G = defaultdict(lambda:list())
    for x in range(W):
        for y in range(H):
            if Ss[y][x] == ".":
                ds = list()
                if x + 1 < W:
                    if Ss[y][x+1] == ".":
                        G[(y,x)].append((y, x+1))
                if x - 1 >= 0:
                    if Ss[y][x-1] == ".":
                        G[(y,x)].append((y, x-1))
                if y + 1 < H:
                    if Ss[y+1][x] == ".":
                        G[(y,x)].append((y+1, x))
                if y - 1 >= 0:
                    if Ss[y-1][x] == ".":
                        G[(y,x)].append((y-1, x))
    MM = 0
    for x in range(W):
        for y in range(H):
            seen = set()
            seen.add((y,x))
            C = G[(y,x)]
            M = 0
            while len(C) != 0:
                M += 1

                C0 = list()
                for k in C:
                    for kk in G[k]:
                        if kk not in seen:
                            C0.append(kk)
                            seen.add(kk)
                C = C0
            MM = max(M, MM)

    print(MM)



main()
