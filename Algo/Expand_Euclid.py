# y > 0
def gcd(x:int, y:int)->int:
    while y != 0:
            x, y = y, x%y
    return x


def lcm(x:int, y:int):
    return x*y//gcd(x, y)

# (参考)https://qiita.com/akebono-san/items/f00c0db99342a8d68e5d

# ax +by = -gcd(a,b)に注意
def ext_gcd(a:int,b:int):
    x, y, u, v = 1, 0, 0, 1
    while b:
        k = a // b
        x -= k * u
        y -= k * v
        x, u = u, x
        y, v = v, y
        a, b = b, a % b
    return x, y
