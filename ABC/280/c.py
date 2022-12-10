def main():
    S = input()
    T = input()

    flag = True
    for i in range(len(S)):
        if S[i] != T[i]:
            ans = i+1
            flag = False
            break

    if flag:
        ans = i+2

    print(ans)


main()
