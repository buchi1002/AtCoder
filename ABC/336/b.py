N = int(input())
cnt = 0
while N%2 == 0:
    cnt += 1
    N //= 2

print(cnt)
