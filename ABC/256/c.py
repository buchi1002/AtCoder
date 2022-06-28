from collections import defaultdict

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())

    sum_3_dic = defaultdict(lambda : [])
    for i in range(1,30+1):
        for j in range(1,30+1):
            for k in range(1,30+1):
                a = [i,j,k]
                key = i+j+k
                sum_3_dic[key] += [[i,j,k]]

    L1 = sum_3_dic[h1]
    L2 = sum_3_dic[h2]
    L3 = sum_3_dic[h3]

    cnt = 0
    for i in L1:
        for j in L2:
            for k in L3:
                if i[0] + j[0] + k[0] == w1 and\
                    i[1] + j[1] + k[1] == w2 and\
                        i[2] + j[2] + k[2] == w3:
                        cnt += 1

    print(cnt)
if __name__ == '__main__':
    main()
