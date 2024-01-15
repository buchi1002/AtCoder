G = [0, 2, 4, 6, 8]
N = int(input())-1

L = list()

ans = 0
e = 0
while N!=0:
    ans += G[(N%5)]*(10**e)
    N//=5
    e += 1


print(ans)
