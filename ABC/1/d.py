def main():
    N = int(input())

    TL = [0]*(60*24+100)
    for i in range(N):
        S,E = map(str, input().split("-"))
        ST = ((int(S[:2])*60 + int(S[2:]))//5)*5
        ET = ((int(E[:2])*60 + int(E[2:]))//5)*5 +\
            (((int(E[:2])*60 + int(E[2:]))%5)!=0)*5
        for i in range(ST,ET+1):
            TL[i] = 1

    cnt = 0
    f = 0
    for i in range(len(TL)):
        if f != TL[i]:
            f = 1-f
            if f == 1:
                S = str(i//60).zfill(2) + str(i%60).zfill(2)
            if f == 0:
                E = str((i-1)//60).zfill(2) + str((i-1)%60).zfill(2)
                print(S + "-" + E)

main()
