N, T = map(int, input().split())
Cs = list(map(int, input().split()))
Ss = set(Cs)
Rs = list(map(int, input().split()))

if T not in Ss:
    T = Cs[0]

M = -1
winner = -1
for i in range(N):
    if Cs[i] == T and M < Rs[i]:
        M = Rs[i]
        winner = i +1

print(winner)
