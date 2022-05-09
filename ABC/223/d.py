def main():
    N, M = map(str, input().split())
    As = [0]*N
    Bs = [0]*N
    prevdic = {"None":"None"}
    latedic = {"None":"None"}

    for i in range(N):
        if i == 0:
            prevdic[Bs[i]] = As[i]
            latedic[As[i]] = Bs[i]
            if As[i] in prevdic and Bs[i] in latedic:
                s = As[i]
                while latedic[s] != Bs[i]:
                    if s == "None":
                        print(-1)
                        break
                s = latedic[s]

            elif As[i] in prevdic and Bs[i] in latedic == 0:


        prevdic[As[i]] = Bs[i]
        latedic[Bs[i]] = As[i]

    s = ""
    checset = {}
    for i in range(M):
        s = str(i)


if __name__ == '__main__':
    main()
