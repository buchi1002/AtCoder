N = int(input())

S1 = {"H", "D", "C", "S"}
S2 = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"}
S3 = set()
f = True
for i in range(N):
    s = input()
    if (s[0] not in S1) or (s[1] not in S2) or (s in S3):
        f = False
    S3.add(s)

if f:
    print("Yes")
else:
    print("No")
