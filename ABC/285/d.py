from collections import defaultdict
import sys

sys.setrecursionlimit(10000000)

def rec(key, d, S, ev, flag):
    if key in ev:
        return

    if key in S:
        flag[0] = False
        return

    S.add(key)

    for k in d[key]:
        rec(k,d,S,ev, flag)

    return

def main():
    N = int(input())

    d = defaultdict(lambda:set())

    flag = [True]
    users = list()
    for _ in range(N):
        s, t = input().split()
        d[s].add(t)
        users.append(s)

    Ss = [set() for _ in range(N)]
    idx = -1
    ev = set()
    for point in users:
        idx += 1
        S = Ss[idx]
        if point not in ev:
            rec(point, d, S, ev, flag)
        ev |= S


    if flag[0]:
        print("Yes")
    else:
        print("No")

main()
