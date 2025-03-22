S = input()
ans = ""
cnt_w = 0
for s in S:
    if s == "W":
        cnt_w += 1
    elif s == "A":
        ans += "A" + "C" * cnt_w
        cnt_w = 0
    else:
        ans += "W" * cnt_w + s
        cnt_w = 0

ans += "W" * cnt_w
print(ans)
