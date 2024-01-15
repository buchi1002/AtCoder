N = int(input())
As = list(map(int, input().split()))

LC = [1]*N
RC = [1]*N

for i in range(1,N):
    if LC[i-1] + 1 <= As[i]:
        LC[i] = LC[i-1]+1
    else:
        LC[i] = min(As[i], i+1)

for i in range(N-2, 0, -1):
    if As[i] >= RC[i+1]+1:
        RC[i] = RC[i+1] + 1
    else:
        RC[i] = min(As[i], N-i)

ans = 0
for i in range(N):
    ans = max(min(RC[i], LC[i]), ans)

print(ans)
