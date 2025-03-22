N, M = map(int, input().split())
Xs = list(map(int, input().split()))
As = list(map(int, input().split()))

XA = [[x, a] for x, a in zip(Xs, As)]
XA.sort(reverse=True)

pri = N
cnt = 0
for i in range(len(XA)):
    x, a = XA[i]
    if pri - x + 1 <= a:
        cnt += (pri-x)*(pri-x+1)//2
        pri = x-1
    else:
        cnt += a*(pri-x + pri-x-a+1)//2
        pri = pri - a
if pri != 0:
    print(-1)
else:
    print(cnt)

if pri < 0:
    for _ in range(10**100):
        for j in range(10):
            1+1
