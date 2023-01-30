S = input()

num = 0
for i in range(len(S)):
    num = num*26 + (ord(S[i]) - 64)

print(num)
