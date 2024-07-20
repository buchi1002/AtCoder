N, A = map(int, input().split())
Ts = list(map(int, input().split()))

t = 0 # 前の人が処理終えた時間
for i in range(N):
    if t < Ts[i]: # 待ち時間なし
        t = Ts[i] + A
    else: # 待ち時間あり
        t = t + A
    print(t)
