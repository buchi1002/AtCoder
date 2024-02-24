def keta(x:int):
    k= 0
    while x != 0:
        k += x%10
        x //= 10

    return k


N = int(input())
k = keta(N)

cnt = 0
for i in range(1, k+1):
