N = int(input())
As = list(map(int, input().split()))
As.sort()

S = sum(As)
RS = [S-As[0]]*(N-1)

for i in range(1,N-1):
    RS[i] = (RS[i-1]-As[i])

print(S)
print(As)
print(RS)

ans = 0
for i in range(N-1):
    ans += RS[i]//As[i]
    print(RS[i]//As[i])

print(ans)
