S = input()
cnt = 0
if S[0] == "o":
    S = "i" + S
    cnt += 1
if S[-1] == "i":
    S = S + "o"
    cnt += 1

for i in range(1, len(S)):
    cnt += S[i-1]==S[i]

print(cnt)