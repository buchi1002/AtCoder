import math

R, X, Y = map(int,input().split())

q = math.floor(math.sqrt((X**2 + Y**2)//(R**2)))
r = (X**2 + Y**2)%(R**2)

if r == 0:
    print(q)
elif X**2 + Y**2 <= 4*(R**2):
    print(2)
else:
    print(q+1)
