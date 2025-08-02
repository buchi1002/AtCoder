from itertools import permutations
points = [tuple(map(int, input().split())) for _ in range(3)]

flag = False
for p1, p2, p3 in permutations(points):
    v1 = (p2[0] - p1[0], p2[1] - p1[1])
    v2 = (p3[0] - p1[0], p3[1] - p1[1])

    if v1[0] * v2[0] + v1[1] * v2[1] == 0:
        flag = True

if flag:
    print("Yes")
else:
    print("No")