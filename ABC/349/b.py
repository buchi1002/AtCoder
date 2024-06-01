from collections import defaultdict
S = input()
d1 = defaultdict(lambda:0)
d2 = defaultdict(lambda:0)

for s in S:
    d1[s] += 1


for k in d1.keys():
    d2[d1[k]] += 1

flag = True
for v in d2.values():
    if v!=2:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")
