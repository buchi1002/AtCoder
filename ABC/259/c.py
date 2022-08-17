def main():
    S = input() + " "
    T = input() + " "

    SCheck = []
    cnt = 0
    s = "##"
    for i in range(len(S)):
        if S[i] == s:
            cnt += 1
            if i == len(S) - 1:
                SCheck.append([s,cnt])
        else:
            if s != "##":
                SCheck.append([s,cnt])
            s = S[i]
            cnt = 1

    TCheck = []
    cnt = 0
    t = "##"
    for i in range(len(T)):
        if T[i] == t:
            cnt += 1
            if i == len(T) - 1:
                TCheck.append([t,cnt])
        else:
            if t != "##":
                TCheck.append([t,cnt])
            t = T[i]
            cnt = 1

    flag = True
    if len(TCheck) != len(TCheck):
        flag = False
    else:
        for i in range(len(TCheck)):
            if TCheck[i][0] != SCheck[i][0]:
                flag = False
                break
            if TCheck[i][1] < SCheck[i][1] or (SCheck[i][1] == 1 and TCheck[i][1] > 1):
                flag = False
                break
        print("Yes"*flag + "No"*(1-flag))
main()
