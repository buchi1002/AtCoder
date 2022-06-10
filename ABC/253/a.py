def main():
    a, b, c = map(int, input().split())
    f = 0
    if a<=b and b <= c:
        f = 1
    elif c <= b and b <= a:
        f = 1
    print("Yes"*f+"No"*(1-f))
if __name__ == '__main__':
    main()
