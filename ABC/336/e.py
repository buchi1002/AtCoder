N = int(input())

k= 0
while N != 0:
    k += N%10
    N //= 10

k
