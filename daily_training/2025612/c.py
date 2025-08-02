N = int(input())
As = [[None]*N for _ in range(N)]

for s in range(N//2 + N%2):
    if s%2 ==0:
        v = "#"
    else:
        v = "."
    for i in range(s, N - s):
        As[i][s] = v
        As[N-i-1][N-s-1] = v
        As[s][i] = v
        As[N-s-1][N-i-1] = v

for i in range(N):
    print("".join(As[i]))