from collections import defaultdict

N, M = map(int,input().split())
Cs = input().split()
Ds = input().split()
Ps = list(map(int,input().split()))

dic = defaultdict(lambda :Ps[0])
for d, p in zip(Ds, Ps[1:]):
    dic[d] = p

print(sum([dic[Cs[i]] for i in range(N)]))
