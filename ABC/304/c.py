import sys
sys.setrecursionlimit(100000000)

def rec(key, G, seen):
    if seen[key]:
        return
    seen[key] = True
    for k in G[key]:
        rec(k, G, seen)
    return

def d(x1, y1, x2, y2):
    return (x1-x2)**2 + (y1-y2)**2

def main():
    N, D = map(int, input().split())
    L = list()
    D2 = D**2

    for i in range(N):
        L.append(list(map(int, input().split())))

    G = [list() for _ in range(N)]
    for i in range(N-1):
        x1, y1 = L[i]
        for j in range(i, N):
            x2, y2 = L[j]

            if d(x1, y1, x2, y2) <= D2:
                G[i].append(j)
                G[j].append(i)

    seen = [False]*N
    rec(0, G, seen)

    for i in range(N):
        if seen[i]:
            print("Yes")
        else:
            print("No")
main()
