N = int(input())
P = [0]*(2*N+2)
As = tuple(map(int, input().split()))
for i in range(N):
    A = As[i]
    P[2*i+2] = P[A]+1
    P[2*i+3] = P[A]+1



[print(P[i]) for i in range(1, 2*N+2)]
