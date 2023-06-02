N, M, H, K = map(int,input().split())
S = input()

healer = set()
for _ in range(M):
    x, y = map(int,input().split())
    healer.add(x*1000000+y)

x = 0
y = 0
cnt = 0
for i in range(N):
    H -= 1
    if S[i] == "R":
        x += 1
    elif S[i] == "L":
        x -= 1
    elif S[i] == "U":
        y += 1
    elif S[i] == "D":
        y -= 1

    if H < 0:
        break
    if (H < K) and (x*1000000+y in healer):
        healer.discard(x*1000000+y)
        H = K

    cnt += 1

if cnt == N:
    print("Yes")
else:
    print("No")
