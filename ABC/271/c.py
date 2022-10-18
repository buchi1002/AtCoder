def main():
    N = int(input())
    As = tuple(map(int, input().split()))
    Read = [0]*(3*(10**5 + 11))

    count = 0
    for a in As:
        if a >= 3*(10**5 + 11):
            count += 1
        else:
            if Read[a] == 0:
                Read[a] = 1
            else:
                count += 1

    s = 1
    e = len(Read) - 1
    while s <= e:
        if Read[s] == 1:
            s += 1
        else:
            if count >= 2:
                Read[s] = 1
                count -= 2
                s += 1
            else:
                if Read[e] == 1:
                    Read[e] = 0
                    count += 1
                e -= 1

    f = 1
    ans = 0
    while f < len(Read) and Read[f] != 0:
        ans += 1
        f += 1

    print(ans)

if __name__ == '__main__':
    main()
