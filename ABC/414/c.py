def main():
    A = int(input())
    N = int(input())
    s = set()
    def isA(X, A):
        check = list()
        while X != 0:
            check.append(X%A)
            X //= A
        return check == check[::-1]

    ans = 0
    for keta in range(1, N):
        if 10 ** (2 * keta - 1) > N:
            break

        for i in range(1, 10 ** keta):
            Ys = str(i).zfill(keta)
            Y = int(Ys[::-1] + Ys[1::])
            if Y <= N and (Y not in s) and isA(Y, A):
                s.add(Y)
                ans += Y

            Xs = str(i).zfill(keta)
            X = int(Xs[::-1] + Xs)

            if X > N:
                continue

            elif X <= N and (X not in s) and isA(X, A):
                s.add(X)
                ans += X

        if Y > N:
            break
    print(ans)

main()