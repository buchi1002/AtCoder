H, W = map(int, input().split())
R, C = map(int, input().split())

# 縦
f = 0
if R == 1:
    f += 1
if R == H:
    f += 1

# 横
if C == 1:
    f += 1
if C == W:
    f += 1

print(4-f)
