N = int(input())
Ss = list()
Cs = list()
for _ in range(N):
    s, c = input().split()
    Ss.append(s)
    Cs.append(int(c))

print(sorted(Ss)[sum(Cs)%N])
