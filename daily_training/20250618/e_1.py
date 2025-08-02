from sortedcontainers import SortedDict

Q = int(input())
s = SortedDict()
qs = [list(map(int, input().split())) for _ in range(Q)]

for q in qs:
    if q[0] == 1:
        x = q[1]
        if x in s:
            s[x] += 1
        else:
            s[x] = 1
    elif q[0] == 2:
        x, c = q[1], q[2]
        if x in s:
            if s[x] <= c:
                del s[x]
            else:
                s[x] -= c
    else:
        print(s.peekitem(-1)[0] - s.peekitem(0)[0])
