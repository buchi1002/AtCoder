As = list()
while True:
    a = int(input())
    As.append(a)
    if a==0:
        break

for a in As[::-1]:
    print(a)