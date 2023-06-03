H, W = map(int, input().split())
ans = list()
for i in range(H):
    S = input()
    S_ = ""
    flag = False
    for j in range(W):
        if flag:
            flag = False
            continue
        elif S[j] == "T" and j + 1 < W and S[j+1] == "T":
            S_ += "PC"
            flag = True
        else:
            S_ += S[j]
    ans.append(S_)

for j in range(H):
    print("".join(ans[j]))
