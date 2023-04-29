def f(x, y, z):
    return (x+y+z)/(x*y*z)

N = int(input())
xs = list(map(int, input().split()))
xs.sort()

p = -1
for i in range(N):
    if xs[i] > 0:
        p = i
        break

if p == -1:
    mini = f(xs[0], xs[1], xs[2])
    maxi = f(xs[N-3], xs[N-2], xs[N-1])

elif p == 0:
    mini = f(xs[N-3], xs[N-2], xs[N-1])
    maxi = f(xs[0], xs[1], xs[2])

else:
    mini = 100
    maxi = -100
    if 3 <= p:
        v = f(xs[0], xs[1], xs[2])
        mini = min(v, mini)
        maxi = max(v, maxi)

        v = f(xs[p-3], xs[p-2], xs[p-1])
        mini = min(v, mini)
        maxi = max(v, maxi)

        v = f(xs[0], xs[p-2], xs[p-1])
        mini = min(v, mini)
        maxi = max(v, maxi)

        v = f(xs[0], xs[1], xs[p-1])
        mini = min(v, mini)
        maxi = max(v, maxi)

    if N - p >= 3:
        v = f(xs[p], xs[p+1], xs[p+2])
        mini = min(v, mini)
        maxi = max(v, maxi)

        v = f(xs[N-3], xs[N-2], xs[N-1])
        mini = min(v, mini)
        maxi = max(v, maxi)

        v = f(xs[p], xs[N-2], xs[N-1])
        mini = min(v, mini)
        maxi = max(v, maxi)

        v = f(xs[p], xs[p+1], xs[N-1])
        mini = min(v, mini)
        maxi = max(v, maxi)

    if 2 <= p and N - p >= 1:
        v = f(xs[p-2], xs[p-1], xs[N-1])
        mini = min(v, mini)
        maxi = max(v, maxi)

        v = f(xs[0], xs[1], xs[p])
        mini = min(v, mini)
        maxi = max(v, maxi)

        v = f(xs[0], xs[1], xs[N-1])
        mini = min(v, mini)
        maxi = max(v, maxi)

        v = f(xs[p-2], xs[p-1], xs[p])
        mini = min(v, mini)
        maxi = max(v, maxi)

    if 1 <= p and N - p >= 2:
        v = f(xs[p-1], xs[N-2], xs[N-1])
        mini = min(v, mini)
        maxi = max(v, maxi)

        v = f(xs[0], xs[p], xs[p+1])
        mini = min(v, mini)
        maxi = max(v, maxi)

        v = f(xs[0], xs[N-2], xs[N-1])
        mini = min(v, mini)
        maxi = max(v, maxi)

        v = f(xs[p-1], xs[p], xs[p+1])
        mini = min(v, mini)
        maxi = max(v, maxi)

print(mini)
print(maxi)
