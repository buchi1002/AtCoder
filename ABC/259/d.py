from collections import defaultdict
import sys
sys.setrecursionlimit(4000)

def func(key,Set,Dic,flag,T):
    if key in Set:
        return flag
    Set.add(key)
    if key == T:
        return True
    for k in Dic[key]:
        flag = func(k,Set,Dic,flag,T)

    return flag


def main():
    N = int(input())
    Sx,Sy,Tx,Ty = map(int,input().split())

    L = []
    snum = -1
    tnum = -1
    for i in range(N):
        x,y,r = map(int,input().split())
        L.append([x,y,r])

        if snum == -1:
            sr = (Sx - x)**2 + (Sy - y)**2
            if sr == r**2:
                snum = i
        if tnum == -1:
            tr = (Tx - x)**2 + (Ty - y)**2
            if tr == r**2:
                tnum = i

    f = False
    D = defaultdict(lambda : set())
    for  i in range(N-1):
        for j in range(i+1,N):
            x0,y0,r0 = L[i]
            x1,y1,r1 = L[j]
            d = (x0-x1)**2 + (y0-y1)**2

            if (r0 + r1)**2 >= d >= abs(r0 - r1)**2:
                D[i].add(j)
                D[j].add(i)

    S = set()
    f = func(snum,S,D,f,tnum)

    print("Yes"*f + "No"*(1-f))
main()
