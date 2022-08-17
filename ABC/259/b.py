import math
a,b,d = map(int,input().split())

D = math.radians(d)
s = math.sin(D)
c = math.cos(D)
X = a*c - b*s
Y = b*c + a*s

print(*[X,Y])
