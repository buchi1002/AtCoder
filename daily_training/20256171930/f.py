from collections import defaultdict
d = defaultdict(set)
N, M, Q = map(int, input().split())
ALL = set(range(1, M+1))
for q in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        _, X, Y = q
        d[X].add(Y)
    elif q[0] == 2:
        _, X = q
        d[X] = ALL
    else:
        _, X, Y = q
        if Y in d[X]:
            print("Yes")
        else:
            print("No")