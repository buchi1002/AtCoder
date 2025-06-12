N = int(input())
Ps = tuple(map(int, input().split()))

i, j = 0, 0
bottom = list()
top = list()
for i in range(1, N-1):
    if Ps[i-1] < Ps[i] > Ps[i+1]:
        top.append(i)
    if Ps[i-1] > Ps[i] < Ps[i+1]:
        bottom.append(i)

t = 0
b = 0
print(top)
print(bottom)
if (t < len(top)) and (b < len(bottom)) and  (top[t] > bottom[b]):
    b += 1

cnt = 0
while (t < len(top)) and (b < len(bottom)):
    left = 0
    right = 0

    if t == 0:
        for j in range(top[t], 0, -1):
            if Ps[j] > Ps[j-1]:
                left += 1
            else:
                break
    else:
        left = (top[t] - bottom[b - 1])

    if t == len(top) - 1:
        for j in range(bottom[b], N-1):
            if Ps[j]  < Ps[j+1]:
                left += 1
            else:
                break
    else:
        right = (top[t + 1] - bottom[b])

    cnt += left * right

    t += 1
    b += 1

print(cnt)