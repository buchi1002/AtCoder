N, K = map(int, input().split())

AB = list()

cnt = 0
for i in range(N):
    a, b = map(int,input().split())
    AB.append((a, b))

    cnt += b

AB.sort(key=lambda x: x[0])

day = 0
if cnt <= K:
    print(day+1)
else:
    for i in range(N):
        cnt -= AB[i][1]
        day = AB[i][0]

        if cnt <= K:
            print(day+1)
            break
