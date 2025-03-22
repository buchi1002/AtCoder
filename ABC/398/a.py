N = int(input())

if N %2 == 1:
    ans = "="
    N -= 1
else:
    ans = "=="
    N -= 2

while N > 0:
    ans = '-' + ans + '-'
    N -= 2

print(ans)
