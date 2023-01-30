N, M = map(int, input().split())

Ss = list()
for i in range(N):
    Ss.append(input()[3:])
Ts = set()
for i in range(M):
    Ts.add(input())

count = 0
for i in range(N):
    if Ss[i] in Ts:
        count += 1

print(count)
