def main():
    L = [set() for i in range(3*10**5+10)]
    S = input()

    Check = set()
    idx = 0
    flag = True
    for i in range(len(S)):
        if S[i] == "(":
            idx += 1

        elif S[i] == ")":
            Check -= L[idx]
            L[idx].clear()

            idx -= 1

        else:
            if S[i] not in Check:
                Check.add(S[i])
                L[idx].add(S[i])

            else:
                flag = False
        if not flag:
            break

    if flag:
        print("Yes")
    else:
        print("No")

main()
