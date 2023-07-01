N = int(input())
S = input()

L = list()
kdict= dict()
close = set()
for i, s in zip(range(N), S):
    if s == "(":
        L.append(i)
    if s == ")":
        if len(L) != 0:
            close.add(L[-1])
            kdict[L[-1]] = i
            L.pop()

ans = ""
idx = 0
while idx < N:
    if idx in close:
        idx = kdict[idx]
    else:
        ans += S[idx]
    idx += 1

print(ans)
