from collections import defaultdict

N = int(input())
As = list(map(int,input().split()))
Q = int(input())

Qs = [defaultdict(lambda:0)]
idx = 0
for i in range(N):
    Qs[idx][i] = As[i]
for _ in range(Q):
    q = tuple(map(int,input().split()))

    if q[0] == 1:
        c = q[1]
        Qs.append(defaultdict(lambda:c))
        idx += 1
    elif q[0] == 2:
         Qs[idx][q[1]-1] += q[2]
    else:
        print(Qs[idx][q[1]-1])
