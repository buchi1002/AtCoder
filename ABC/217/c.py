def main():
    N = int(input())
    Ps = list(map(int, input().split()))
    Qs = [0]*N

    for i in range(N):
        Qs[Ps[i]-1] = i+1

    print(*Qs)
if __name__ == '__main__':
    main()
