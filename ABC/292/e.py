import sys
sys.setrecursionlimit(20000)

def rec(key, G, seen, L):
    if key in seen:
        return
    seen.add(key)
    L.append(key)

    for k in G[key]:
        rec(k, G, seen, L)
    return

def main():
    N, M = map(int, input().split())
    G0 = [[False]*N for _ in range(N)]
    G1 = [list() for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u, v = u-1, v-1

        G0[u][v] = True
        G1[u].append(v)

    c = 0
    for u in range(N):
        seen0 = set()
        L = list()
        rec(u, G1, seen0, L)

        for v in L:
            if u != v and not G0[u][v]:
                c += 1

    print(c)

main()
