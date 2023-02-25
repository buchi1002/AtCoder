def rfunc(el,p):
    m = p
    a, la = 0, 1
    while p != 0:
        q = el // p
        el, p = p, el % p
        a, la = la-q*a, a
    return la % m

p = 13
for i in range(10):
    print(rfunc(i,p))

print(int("10000000111",2))
