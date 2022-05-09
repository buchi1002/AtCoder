N, A, B = map(int, input().split())

def func(x):
    if x==0:
        return "."
    else:
        return "#"


for i in range(N*A):
    s = ""
    f1 = (i//A)%2
    for j in range(N*B):
        f2 = (j//B)%2
        s += func((f1+f2)%2)

    print(s)
