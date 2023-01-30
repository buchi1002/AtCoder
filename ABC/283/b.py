N = int(input())
As = list(map(int,input().split()))
Q = int(input())

for _ in range(Q):
    q = input()
    if q[0] == "1":
        _, k,x = map(int,q.split())
        As[k-1] = x
    else:
        _, k = map(int,q.split())
        print(As[k-1])
