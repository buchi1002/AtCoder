N, Q = map(int, input().split())
J = [0]*N

for q in range(Q):
    n, x = map(int, input().split())
    if n == 1:
        J[x-1] += 1
    elif n == 2:
        J[x-1] = 2
    else:
        if J[x-1] == 2:
            print("Yes")
        else:
            print("No")
