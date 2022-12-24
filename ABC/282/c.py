def main():

    N = int(input())
    S = input()

    flag = False
    s = list()
    for i in range(N):
        if S[i] == '"':
            flag = not flag
            s.append('"')
        else:
            if flag:
                s.append(S[i])
            else:
                if S[i] == ",":
                    s.append(".")
                else:
                    s.append(S[i])

    print("".join(s))
main()
