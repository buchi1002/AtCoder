from math import sqrt, sin, cos, pi
A, B, H, M = map(int, input().split())
hx = A * cos((2 * pi) * ((M / 60 + H) / 12))
hy = A * sin((2 * pi) * ((M / 60 + H) / 12))

mx = B * cos((2 * pi) * (M / 60))
my = B * sin((2 * pi) * (M / 60))

length = (hx - mx) ** 2 + (hy - my) ** 2

print(sqrt(length))