S = input()
T = input()

bm = [False]*len(T)
am = [False]*len(T)
for i in range(len(T)):
    if S[i] == T[i] or S[i] == "?" or T[i] == "?":
        bm[i] = True

    if S[-len(T) + i] == T[i] or S[-len(T) + i] == "?" or T[i] == "?":
        am[i] = True


error = len(T) - sum(am)

if error == 0:
    print("Yes")
else:
    print("No")

for x in range(len(T)):
    if am[x] == False and bm[x] == True:
        error -= 1
    if am[x] == True and bm[x] == False:
        error += 1

    if error == 0:
        print("Yes")
    else:
        print("No")
