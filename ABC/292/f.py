from math import sqrt
def f(r, A, B):
    return r**2 - 2*B*sqrt(r**2 - A**2) - 2*A*sqrt(r**2-B**2)

def df(r, A, B):
    return 2*r - (2*B*r/sqrt(r**2 - A**2)) - (2*A*r/sqrt(r**2 - B**2))

A, B = map(int, input().split())
A, B = min(A, B), max(A, B)

if 4*A*A <= 3*B*B:
    print(A*2/sqrt(3))
elif A == B:
    print((sqrt(6)-sqrt(2))*A)
else:
    r = B  + 0.1
    v = f(r, A, B)
    t  = 0
    while abs(v) > 1/(10**9):
        r = r - f(r, A, B)/df(r, A, B)
        v = f(r, A, B)

        t += 1

        if t > 100000 or abs(df(r, A, B)) < 0.001:
            break

    print(r)
