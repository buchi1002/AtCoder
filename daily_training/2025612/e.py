N, W = map(int, input().split())

ABs = list()

for i in range(N):
    a, b = map(int, input().split())
    ABs.append((a, b))

ABs.sort()

used = 0
v = 0
while used < W and len(ABs) > 0:
    a, b = ABs.pop()
    if b <= W - used:
        v += a*b
        used += b
    else:
        v += a*(W-used)
        used = W

print(v)