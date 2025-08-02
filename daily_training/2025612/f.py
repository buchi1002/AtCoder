N = int(input())
M = 1
for i in range(2, 10**6+10):
    if i**3 <= N:
        s = str(i**3)
        if s==s[::-1]:
            M = i**3

print(M)