N = int(input())
As = tuple(map(int,input().split()))
m = 1<<40
if len(As) == 1:
    print(As[0])
else:
    for i in range(1<<(N-1)):
        bit = bin(i)[2:].zfill(N-1)

        v = As[0]
        l = list()

        for j in range(len(bit)):
            if bit[j] == "0":
                v = v|As[j+1]
            else:
                l.append(v)
                v = As[j+1]
        l.append(v)

        s = l[0]
        for x in range(1,len(l)):
            s = s^l[x]
        m = min(s,m)

    print(m)
