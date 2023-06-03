from itertools import permutations
N, M = map(int, input().split())
Ss = [input() for _ in range(N)]

flag_e = False
for Ss_ in permutations(Ss, N):
    flag = True
    for i in range(N-1):
        cnt = 0
        for j in range(M):
            cnt += Ss_[i][j] != Ss_[i+1][j]
        if cnt >= 2:
            flag = False
    flag_e = flag_e or flag

if flag_e:
    print("Yes")
else:
    print("No")
