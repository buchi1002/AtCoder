def main():
    N, X = map(int, input().split())
    As = list(map(int, input().split()))
    S = set(As)

    flag = False
    for a in As:
        if a + X in S:
            flag = True
            break

    if flag:
        print("Yes")

    else:
        print("No")

main()
