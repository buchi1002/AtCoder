def main():
    N, K = map(int,input().split())
    print(((K-1)*(N-K)*6 + 3*(K-1)+3*(N-K) + 1)/(N**3))
if __name__ == '__main__':
    main()
