M = int(input())

i = 0
q = M//3
r = M%3
As = [i]*r
while q != 0:
    i += 1
    q, r = q//3, q%3
    for _ in range(r):
        As.append(i)
print(len(As))
print(*As)