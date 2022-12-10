N = int(input())
Ss = list(map(int, input().split()))

As = list()
As.append(Ss[0])

for i in range(1,N):
    As.append(Ss[i]-Ss[i-1])

print(*As)
