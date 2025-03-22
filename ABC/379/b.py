N, K = map(int, input().split())
S = input()

flag = True
cnt = 0
cont = 0
for i in range(N):
    if S[i]=="O":
        cont += 1
    else:
        cnt += cont//K
        cont = 0
cnt += cont//K
print(cnt)
