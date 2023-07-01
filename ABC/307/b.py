N = int(input())
Ss = list()

for i in range(N):
    Ss.append(input())

flag = False
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        S = Ss[i] + Ss[j]
        S_i = ""
        for k in range(1, len(S)+1):
            S_i += S[-k]

        if S_i == S:
            flag = True

if flag:
    print("Yes")
else:
    print("No")
