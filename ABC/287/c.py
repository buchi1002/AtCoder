from collections import defaultdict
import sys

sys.setrecursionlimit(10000000)


def rec(key):
    if key in s:
        return
    s.add(key)

    for k in d[key]:
        rec(k)

    return

N, M = map(int,input().split())
d = defaultdict(lambda:set())

for i in range(M):
    u, v = map(int,input().split())
    d[u].add(v)
    d[v].add(u)

if M != N - 1:
    print("No")
else:
    s = set()
    rec(1)

    flag = True
    haji = 0
    naka = 0
    for i in range(1,N+1):
        if len(d[i]) == 1:
            haji += 1
        if len(d[i]) == 2:
            naka += 1

    if haji != 2 or haji + naka != N:
        flag = False

    if len(s) != N:
        flag = False

    if flag:
        print("Yes")
    else:
        print("No")
