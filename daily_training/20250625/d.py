N, M = map(int, input().split())

INF = float("inf")

X = 0
v = 1
for _ in range(M + 1):
    X += v
    if X > 10**9:
        X = INF
        break
    v *= N

print(X)