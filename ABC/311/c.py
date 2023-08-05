N = int(input())
As = list(map(int, input().split()))
As = [a-1 for a in As]

seen = [False for i in range(N)]

v = 0
ans = []
while not seen[v]:
    seen[v] = True
    ans.append(v+1)

    v = As[v]

idx = 0
for i in range(len(ans)):
    if ans[i] == v+1:
        idx = i
        break

print(len(ans[i:]))
print(*ans[i:])
