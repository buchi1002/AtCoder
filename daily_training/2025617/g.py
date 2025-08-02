from sys import setrecursionlimit
setrecursionlimit(10**6)

N, x, y = map(int, input().split())
As = list(map(int, input().split()))

def rec(G:list[list], seen:list[bool], key:int):
    if seen[key]:
        return
    seen[key] = True
    for k in G[key]:
        rec(G, seen, k)
