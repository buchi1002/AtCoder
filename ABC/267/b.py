def main():
    S = input()

    flag = False
    if S[0] == "1":
        print("No")
    else:
        D = S[6] + S[3] + str(int(S[7])|int(S[1])) + str(int(S[4])|int(S[0])) + str(int(S[8])|int(S[2])) + S[5] + S[9]
        D = D.split("0")
        cnt = 0
        for i in D:
            if i != "":
                cnt += 1

        if cnt >= 2:
            print("Yes")
        else:
            print("No")
if __name__ == '__main__':
    main()
