N, Q = map(int, input().split())
d = {"R":(1, 0), "L":(-1, 0), "U":(0, 1), "D":(0, -1)}
L = list([i, 0] for i in range(N, 0, -1))
head = N
for _ in range(Q):
    s = input()
    if s[0] == "1":
        _, C = s.split()
        L.append([L[-1][0] + d[C][0], L[-1][1] + d[C][1]])
        head += 1
    else:
        _, p = s.split()
        p = int(p)
        print(*L[head - p])