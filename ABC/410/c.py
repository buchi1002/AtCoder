N, Q = map(int, input().split())
As = list(range(1, N + 1))
start = 0
for _ in range(Q):
    q = input()
    if q[0] == "1":
        _, p, x = map(int, q.split())
        As[(start + p-1)%N] = x
    elif q[0] == "2":
        _, p = map(int, q.split())
        print(As[(start + p-1)%N])
    else:
        _, k = map(int, q.split())
        start = (start + k)%N