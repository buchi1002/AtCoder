def main():
    N = int(input())
    As = [0]*N
    Bs = [0]*N

    L = 0
    for i in range(N):
        As[i], Bs[i] = map(int, input().split())
        L += As[i]/Bs[i]
    point = L/2

    check = 0
    sum = 0
    num = 0
    for i in range(N):
        if sum + As[i]/Bs[i] > point:
            break

        sum += As[i]/Bs[i]
        check += As[i]
        num = i

    if num + 1 > N - 1:
        num -= 1
    check += (point - sum)*Bs[num+1]

    print(check)
if __name__ == '__main__':
    main()
