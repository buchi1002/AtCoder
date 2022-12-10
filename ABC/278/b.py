H, M = map(int, input().split())

while True:
    A = str(H).zfill(2)[0]
    B = str(H).zfill(2)[1]
    C = str(M).zfill(2)[0]
    D = str(M).zfill(2)[1]

    B, C = C, B

    if 0<=int(A+B)<=23 and 0<=int(C+D)<=59:
        break
    else:
        M = (M + 1)%60
        H = (H + (M==0))%24

print(*[H, M])
