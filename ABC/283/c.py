S = input()

flag = False
count = 0
for i in range(len(S)):
    if S[i] != "0":
        count += 1
        flag = False
    else:
        if flag:
            flag = False
        else:
            count += 1
            flag = True

print(count)
