N = int(input())
S = input()

for i in range(1,N):
    m = 0
    for k in range(N - i):
        if S[k] != S[k+i]:
            m = k+1
        else:
            break
    print(m)
