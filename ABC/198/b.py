N = input()
p = 0
for i in range(10):
    if list(N) == list(reversed(list(N))):
        print('Yes')
        p = 1
        break
    N = '0' + N
if p == 0:
    print('No')
