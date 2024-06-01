N = int(input())
As = list(map(int, input().split()))
As.sort()

ans = 0
for i in range(N):
    ans += As[i]*(N-1)

s = 0
e0 = N-1
e1 = N
while s < e0:
    if As[s] + As[e0] >= 10**8:
        ans -= (e0-s)*(e1-e0)*(10**8)
        e1 = e0
        e0 -= 1
    while e0 > s and As[s] + As[e0] >= 10**8:
        ans -= 10**8
        e0 -= 1
    s += 1


print(ans)
