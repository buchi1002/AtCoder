K = "12345"

k = 0

for i in range(len(K)):
    k += int(K[-i])*(10**i)

print(k)
