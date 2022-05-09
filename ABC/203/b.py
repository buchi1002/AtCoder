def main():
    # input
    N, K = map(int, input().split())
    # computep
    # output
    print(int((1/2)*N*(N+1)*100*K + (1/2)*K*(K+1)*N))
if __name__ == '__main__':
    main()
