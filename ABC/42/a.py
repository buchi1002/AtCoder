def main():
    A,B, C = map(int, input().split())
    f = A*B*C ==5*7*5
    print("YES"*f+"NO"*(1-f))
if __name__ == '__main__':
    main()
