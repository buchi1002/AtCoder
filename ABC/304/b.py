N = input()
L = len(N)
if L <= 3:
    print(int(N))
else:
    print(int(N[:3] + "0"*(L-3)))
