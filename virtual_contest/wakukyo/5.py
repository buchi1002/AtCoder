from sys import setrecursionlimit
setrecursionlimit(10**7)
def rec(key):
    if seen[key]:
        return
    else:
        seen[key] = True
        ANS[0] += 1
        if ANS[0] >= 10**6:
            return
    
        for k in G[key]:
            rec(k)    
            if ANS[0] >= 10**6:
                return
        seen[key] = False
        return

N, M = map(int, input().split())
G = [list() for _ in range(N)]

for i in range(M):
    u, v = map(int, input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)

seen = [0]*N
ANS = [0]
rec(0)
print(min(10**6, ANS[0]))