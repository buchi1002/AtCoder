N, Y = map(int, input().split())
a, b, c = -1,-1,-1
for i in range(N+1):
    res = Y - 5000*i
    n = N - i
    r = (res%10000)//1000
    q = res//10000
    x = (n-q-r)//9
    if ((n-q-r)%9==0) and (q+r <= n <= 10*q+r):
        a, b, c = q -x, i, r+10*x
        break

print(a, b, c)
