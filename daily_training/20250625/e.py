from sortedcontainers import SortedSet
N = int(input())
L = SortedSet(range(1, 2 * N + 2))

for i in range(N):
    print(L[0])
    L.discard(L[0])
    x = int(input())
    L.discard(x)

print(L[0])