def main():
    N, Q = map(int,input().split())
    S = input()
    idx = 0
    for _ in range(Q):
        n,x = input().split()
        x = int(x)
        if n == "1":
            idx = (idx - x)%N
        if n == "2":
            print(S[(idx  + x-1)%N])
if __name__ == '__main__':
    main()
