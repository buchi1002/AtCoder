N = int(input())
As = list(map(int, input().split()))

next = 0
for i in range(N-1):
    s, t = map(int, input().split())
    money = 0
    money = As[i] + next
    next = 0

    next = (money//s)*t

print(next + As[-1])
