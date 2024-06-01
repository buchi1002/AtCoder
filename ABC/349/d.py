def main():
    L, R = map(int, input().split())

    ans = list()
    while L < R:
        exp = 1
        while L%(exp<<1) == 0 and (L//(exp<<1)+1)*(exp<<1) <= R:
            exp = (exp << 1)

        ans.append([L, exp*(L//exp+1)])
        L = exp*(L//exp+1)

    print(len(ans))
    [print(*a) for a in ans]
main()
