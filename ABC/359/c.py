Sx, Sy = map(int, input().split())
Tx, Ty = map(int, input().split())

Sx = Sx -(Sx+Sy)%2
Tx = Tx -(Tx+Ty)%2

h = abs(Ty-Sy)
w = abs(Tx-Sx)

x, y = Sx, Sy
cost = h

if Tx > Sx:
    x = min(Sx+h+1, Tx) - (min(Sx+h+1, Tx)+Ty)%2
    cost += (Tx-x)//2
elif Sx > Tx:
    x = max(Sx-h, Tx) - (max(Sx-h, Tx)+Ty)%2
    cost += (x-Tx)//2

print(cost)
