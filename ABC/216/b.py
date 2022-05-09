N = int(input())

dic = {}
k = 0
for i in range(N):
    X = str(input())
    if X in dic:
            k = 1
            break
    dic[X] = "1"


if k == 1:
    print("Yes")
else:
    print("No")
