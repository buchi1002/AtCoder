import itertools

H, W = map(int, input().split())
As = list()

for _ in range(H):
    a = list(map(int, input().split()))
    As.append(a)


cnt = 0
P = list(range(H+W-2))
for Z in itertools.combinations(P, H-1):
    sZ = set(Z)

    seen = set()
    seen.add(As[0][0])
    flag = True
    x = 0
    y = 0
    for te in range(H+W-2):
        if te in sZ:
            y += 1
        else:
            x += 1

        if As[y][x] in seen:
            flag = False
            break

        seen.add(As[y][x])

    if flag:
        cnt += 1

print(cnt)
