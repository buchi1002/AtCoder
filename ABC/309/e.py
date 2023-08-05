import sys

sys.setrecursionlimit(100000000)


def dfs(G, key, seen, ins, v, cnt):
    if seen[key]:
        return

    seen[key] = True

    if v >= 0 or ins[key] >= 1:
        cnt[0] += 1

    for k in G[key]:
        dfs(G, k, seen, ins, max(v-1, ins[k]), cnt)

    return



def main():
    N, M = map(int, input().split())

    Ps = [1] + list(map(int, input().split()))
    G = [list() for _ in range(N)]
    for i in range(1, N):
        a, b = i, Ps[i]-1
        G[a].append(b)
        G[b].append(a)

    ins = [-1 for _ in range(N)]
    for i in range(M):
        x, y = map(int, input().split())
        ins[x-1] = max(ins[x-1], y)

    cnt = [0]
    seen = [False]*N
    dfs(G, 0, seen, ins, ins[0], cnt)

    print(*cnt)

main()
