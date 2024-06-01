N = int(input())
As = list(map(int, input().split()))
Es = list(map(lambda x:len(str(x)), As))

v = 0
for i in range(N):
    v += pow(10, Es[i])

for i in range(N):
    v -= pow(10, Es[i])
    Es[i] = v

ans = 0
for i in range(N):
    ans = (ans + As[i]*Es[i] + As[i]*i)%998244353

print(ans)
