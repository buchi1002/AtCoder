N = int(input())

S = ""
for _ in range(N):
    c, l = input().split()
    if int(l) > 100:
        S = "Too Long"
    else:
        S += c * int(l)

if len(S) > 100:
    print("Too Long")
else:
    print(S)