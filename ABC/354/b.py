N = int(input())
Ss,T = list(),0
for i in range(N):
    s, c = input().split()
    Ss.append(s)
    T += int(c)

Ss.sort()
print(Ss[T%N])
