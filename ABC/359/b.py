N = int(input())
cs = [[-1, -1] for _ in range(N)]
As = list(map(int, input().split()))
for i in range(2*N):
    if cs[As[i]-1][0] == -1:
        cs[As[i]-1][0] = i
    else:
        cs[As[i]-1][1] = i

cnt = 0
for c in cs:
    if c[1] - c[0] == 2:
        cnt += 1

print(cnt)
