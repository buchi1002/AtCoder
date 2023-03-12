import sys
sys.setrecursionlimit(100000000)

def rec(key, G, seen, groups):
    if seen[key]:
        return
    seen[key] = True
    groups[-1].append(key)
    for k in G[key]:
        rec(k, G, seen, groups)
    return


def main():
    N, M = map(int, input().split())
    G = [list() for _ in range(N)]

    for i in range(M):
        u, v = map(int, input().split())
        u, v = u-1, v-1
        G[u].append(v)
        G[v].append(u)

    seen = [False]*N
    groups = [list()]
    for i in range(N):
        if seen[i] == False:
            groups.append(list())
            rec(i, G, seen, groups)

    flag = True
    for g in groups:
        e = 0
        for v in g:
            e += len(G[v])

        if e//2 != len(g):
            flag = False
            break

    if flag:
        print("Yes")
    else:
        print("No")

main()
