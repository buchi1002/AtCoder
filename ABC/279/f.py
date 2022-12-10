def indicate(dic, key):
    if key == dic[key]:
        return key
    else:
        return indicate(dic, dic[key])

def main():
    N, Q = map(int,input().split())
    count = N-1
    D = [0]*N
    dic = dict()
    dicb = dict()
    for i in range(N):
        dic[i] = i
        dicb[i] = i

    for i in range(Q):
        op = input()
        if op[0] == "1":
            _, X, Y = map(int, op.split())
            dic[(Y-1) + (10**8)*D[(Y-1)]] = X-1
            D[(Y-1)] += 1

        elif op[0] =="2":
            _, X = map(int, op.split())
            count += 1
            dicb[count] = (10**8)*D[(X-1)] + (X-1)
            dic[(X-1) + (10**8)*D[X-1]] = (X-1) + (10**8)*D[X-1]

        else:
            _, X = map(int, op.split())
            print(indicate(dic, dicb[X-1])%(10**8) + 1)
    print(dic)

main()
