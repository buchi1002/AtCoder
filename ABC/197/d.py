import math

N = int(input())
x0, y0 = map(int,input().split())
x2, y2 = map(int,input().split())

xs, ys = (x0+x2)/2, (y0+y2)/2

vx0, vy0 = x0 -xs, y0 - ys

vx1 = vx0*math.cos(2*math.pi/N) - vy0*math.sin(2*math.pi/N)
vy1 = vy0*math.cos(2*math.pi/N) + vx0*math.sin(2*math.pi/N)

print(*[vx1 + xs, vy1 + ys])
