def main():
    L1, R1, L2, R2 = map(int,input().split())
    cnt = 0
    for i in range(101):
        if (L1 <= i <= R1) and (L2 <= i <= R2):
            cnt += 1

    print(max(0,cnt-1))
if __name__ == '__main__':
    main()
