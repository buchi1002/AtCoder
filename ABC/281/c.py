N, T = map(int,input().split())
As = list(map(int,input().split()))

roop = sum(As)

T = T%roop

for i in range(len(As)):
    if T - As[i] < 0:
        print(*[i+1, T])
        break
    else:
        T -= As[i]
