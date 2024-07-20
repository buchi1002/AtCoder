N = int(input())
Ls = list()
Rs = list()
Xs = list()
for i  in range(N):
    L, R = map(int, input().split())
    Xs.append(L)
    Ls.append(L)
    Rs.append(R)

if sum(Ls) > 0 or sum(Rs) < 0:
    print("No")
else:
    V = sum(Ls)
    for i in range(N):
        if V < 0:
            if V + (Rs[i] - Ls[i]) < 0:
                Xs[i] = Rs[i]
                V += (Rs[i]-Ls[i])
            else:
                Xs[i] += -V
                V = 0
    print("Yes")
    print(*Xs)
