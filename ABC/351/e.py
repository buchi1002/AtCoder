def Re(R):
    RR = sum(R)
    ans = RR
    for i, e in enumerate(R):
        len(R)-
N = int(input())
Ox = list()
Oy = list()
Ex = list()
Ey = list()

for _ in range(N):
    x, y = map(int, input().split())
    if not bool((x+y)%2):
        Ox.append(x)
        Oy.append(y)
    else:
        Ex.append(x)
        Ey.append(y)

Ox.sort()
Oy.sort()
Ex.sort()
Ey.sort()

OXX = sum(Ox)
for i in Ox:
    OX -=
