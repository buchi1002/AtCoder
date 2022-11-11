H, W = map(int, input().split())

a = [0]*W
for i in range(H):
    c = input()
    for j in range(W):
        a[j] += (c[j] == "#")

print(*a)
