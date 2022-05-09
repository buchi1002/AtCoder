def Base_change(b, n):
    nlen = len(n)

    out = 0
    for i in range(1,nlen+1):
        out = int(n[-i])*(b**(i-1)) + out
    return(out)

K = int(input())
A, B = map(str, input().split())
print(Base_change(K, A)*Base_change(K, B))
