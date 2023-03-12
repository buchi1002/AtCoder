N = int(input())

count = [0]*2*(10**5+10)

for i in range(1,N):
    for j in range(1,N):
        if j*j > i:
            break
        if i%j == 0:
            count[i] += 2
        if j*j == i:
            count[i] -= 1

ans = 0
for i in range(1, N):
    ans += count[i]*count[N-i]

print(ans)
