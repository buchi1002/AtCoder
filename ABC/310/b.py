N, M = map(int,input().split())
Cs = [list(map(int, input().split())) for _ in range(N)]

Cs.sort(key=lambda x: -x[0])

flag = False
for i in range(N-1):
    Ci = set(Cs[i][2:])
    for j in range(i, N):
        Cj = set(Cs[j][2:])
        if Cj >= Ci:
            if Cs[i][0] > Cs[j][0] or Cs[i][1] < Cs[j][1]:
                flag = True

if flag:
    print("Yes")
else:
    print("No")
