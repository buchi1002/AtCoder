from collections import defaultdict
N, R, C = map(int, input().split())
S = input()
seen = defaultdict(lambda : len(S) + 10)
x, y = 0, 0
seen[(x, y)] = len(S)
for i, s in enumerate(S[::-1]):
    if s == "N":
        y -= 1
    elif s == "S":
        y += 1
    elif s == "E":
        x += 1
    else:
        x -= 1
    seen[(x, y)] = len(S) - i - 1

R, C = R + y , C + x
for i, s in enumerate(S):
    if s == "N":
        R += 1
    elif s == "S":
        R -= 1
    elif s == "E":
        C -= 1
    else:
        C += 1
    if seen[(C, R)] != -1 and seen[(C, R)] <= i + 1:
        print(1, end = "")
    else:
        print(0, end = "")
print("\n")
