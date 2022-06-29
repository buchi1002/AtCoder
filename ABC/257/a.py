def main():
    N,X = map(int,input().split())
    s = ""
    for i in range(26):
        s += chr(65+i)*N
    print(s[X-1])
if __name__ == '__main__':
    main()
