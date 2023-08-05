N = int(input())
Ps = list()
for i in range(N):
    a, b = map(int, input().split())
    Ps.append([i+1, a*10000000000000000000//(a+b)])


print(*[x[0] for x in sorted(Ps, key = lambda x: -x[1])])
