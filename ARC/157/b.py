N, K = map(int, input().split())
S = input()

nx = S.count("X")
ny = len(S) - nx

if K == 0:
    count = 0
    for i in range(1, N):
        if S[i-1] == S[i] == "Y":
            count += 1

    print(count)

elif 1 <= K < nx:
    Vs = list()
    for i in range(N):
        if S[i] == "X":
            Vs.append(0)
        else:
            Vs.append(1)
    Xs = [list()]
    for i in range(N):
        if S[i] == "X":
            if i == 0 or i == N-1:
                Xs[-1].append(-1)
            Xs[-1].append(i)
        else:
            if len(Xs[-1]) != 0:
                Xs.append(list())
    Xs.sort(key=lambda x:len(x))

    count = K
    for xs in Xs:
        for j in xs:
            if j == -1:
                continue
            if count - 1 >= 0:
                Vs[j] = 1
                count -= 1
            else:
                break
    count = 0
    for i in range(1, N):
        if Vs[i-1] == Vs[i] == 1:
            count += 1
    print(Xs)
    print(Vs)
    print(count)
else:
    if S[0] == "Y":
        print(N - (K - nx) - 1)
