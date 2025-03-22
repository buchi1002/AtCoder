from collections import defaultdict
As = list(map(int, input().split()))

ful = False
for i in range(1, 13+1):
    for j in range(1, 13+1):
        if i==j:
            continue
        n_i = 0
        n_j = 0
        for a in As:
            if a == i:
                n_i += 1
            if a == j:
                n_j += 1
        if n_i >= 3 and n_j >= 2:
            ful = True

if ful:
    print("Yes")
else:
    print('No')
