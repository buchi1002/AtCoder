N, S = map(int, input().split())
Ts = list(map(int, input().split()))
Ts = [0] + Ts
if all(Ts[i+1]-Ts[i] <= S for i in range(N)):
    print("Yes")
else:
    print("No")