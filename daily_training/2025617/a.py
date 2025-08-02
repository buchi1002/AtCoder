S = input()

n = 0
ans = ""
for s in S:
    if s =="|":
        n += 1
        continue
    if n != 1:
        ans += s

print(ans)