S = input()

B1 = 10
B2 = 0
for i in range(8):
    if S[i] == "B":
        B1 = min(B1, i)
        B2 = max(B2, i)
flag1 = B1%2 != B2%2

R1 = 10
R2 = 0
K = 0
for i in range(8):
    if S[i] == "R":
        R1 = min(R1, i)
        R2 = max(R2, i)
    if S[i] == "K":
        K = i
flag2 = R1 < K < R2

flag = flag1 and flag2

if flag:
    print("Yes")
else:
    print("No")
