H = int(input())

n = 1
for i in range(1,100):
    if H < n:
        print(i)
        break
    n += 2**i
