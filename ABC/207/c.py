def main():
    # input
    N = int(input())
    ts = [0]*N
    ls = [0]*N
    rs = [0]*N

    for i in range(N):
        ts[i], ls[i], rs[i] = map(int, input().split())
        if ts[i] == 2:
            rs[i] -= 0.3
        elif ts[i] == 3:
            ls[i] += 0.3
        elif ts[i] == 4:
            ls[i] += 0.3
            rs[i] -= 0.3
    # compute
    count = 0
    s = 0
    for i in range(N):
        for j in range(i+1,N):
            s += 1
            if(rs[j]-ls[i])*(rs[i]-ls[j]) >= 0:
                count  += 1
    # output
    print(count)
if __name__ == '__main__':
    main()
