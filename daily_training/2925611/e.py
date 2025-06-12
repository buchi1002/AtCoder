N, M = map(int, input().split())
As = list(map(int, input().split()))

l = 0
r = M + 1
while r - l > 1:
    x = (l + r)//2
    cnt = 0
    for i in range(N):
        cnt += min(As[i], x)
    if cnt > M:
        r = x
    else:
        l = x    

print(l if l < M else "infinite")