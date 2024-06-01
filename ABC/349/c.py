S = input() + "x"
T = input()


idx = 0
t = ""
for s in S:
    if s.upper() == T[idx]:
        t += s.upper()
        idx += 1

    if idx == 3:
        break


flag = (t == T)

if flag:
    print("Yes")
else:
    print("No")
