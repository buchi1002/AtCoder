from collections import defaultdict

S = input()
T = input()

d = defaultdict(lambda:[0, 0])

for key in {"a", "t", "c", "o", "d", "e", "r", "@"}:
    d[key]

for s in S:
    d[s][0] += 1
for t in T:
    d[t][1] += 1

flag = True
for key in d.keys():
    if not (key in {"a", "t", "c", "o", "d", "e", "r", "@"}):
        if d[key][0] != d[key][1]:
            flag = False
            break

for key in d.keys():
    if key in {"a", "t", "c", "o", "d", "e", "r"}:
        if d[key][0] > d[key][1]:
            d["@"][1] -= (d[key][0] - d[key][1])
        else:
            d["@"][0] -= (d[key][1] - d[key][0])

        if d["@"][0] < 0 or d["@"][1] < 0:
            flag = False
            break

if flag:
    print("Yes")
else:
    print("No")
