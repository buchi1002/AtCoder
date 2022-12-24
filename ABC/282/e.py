N = int(input())
S = input()

flag = False
s = ""
for i in range(N):
    if S[i] == '"':
        flag = not flag
        s += '"'
    else:
        if flag:
            s += S[i]
        else:
            if S[i] == ",":
                s += "."
            else:
                s += S[i]

print(s)
