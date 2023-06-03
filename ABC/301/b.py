N = int(input())
As = list(map(int, input().split()))

L = list()
for i in range(N-1):
    if As[i] < As[i+1]:
        L += list(range(As[i], As[i+1]))
    else:
        L += list(range(As[i], As[i+1], -1))

L.append(As[-1])
print(*L)
