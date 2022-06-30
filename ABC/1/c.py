Deg, Dis = map(int,input().split())
L = ["N", "NNE", "NE", "ENE", "E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]

dir = L[((Deg*10 + 1125)//2250)%16]

Dis = Dis/60 + 0.00001
a = 0.1*((Dis*100)%10 + 0.00001 >= 5)
Dis += a

p = -1 + (Dis>=0) + (Dis>=0.3) + (Dis>=1.6) + (Dis>=3.4) + (Dis>=5.5) + (Dis>=8.0) + (Dis>=10.8) + (Dis>=13.9) + (Dis>=17.2) + (Dis>=20.8) + (Dis>=24.5) + (Dis>=28.5) + (Dis>=32.7)

if p == 0:
    dir = "C"

print(*[dir,p])
