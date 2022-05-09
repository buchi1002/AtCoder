def main():
    Ss = [""]*4
    Ss[1] = input()
    Ss[2] = input()
    Ss[3] = input()
    T = input()

    L = len(T)
    Ans = ""
    for i in range(L):
        Ans = Ans + Ss[int(T[i])]

    print(Ans)
if __name__ == '__main__':
    main()
