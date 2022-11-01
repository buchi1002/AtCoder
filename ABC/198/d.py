import itertools

def main():
    ERROR = "UNSOLVABLE"
    S1 = input()
    S2 = input()
    S3 = input()

    Ss = set()
    for s in S1:
        Ss.add(s)
    for s in S2:
        Ss.add(s)
    for s in S3:
        Ss.add(s)

    Ss = list(Ss)
    k = len(Ss)
    if k >= 11:
        print(ERROR)
        return

    else:
        dic = dict()
        L = tuple(range(10))
        flag = False
        for p in itertools.permutations(L, k):
            if flag:
                break
            for i in range(k):
                dic[Ss[i]] = p[i]

            if dic[S1[0]] == 0 or dic[S2[0]] == 0 or dic[S3[0]] == 0:
                continue

            s1, s2, s3 = 0, 0, 0
            for i in range(len(S1)):
                s1 += dic[S1[len(S1)-1-i]]*(10**i)
            for i in range(len(S2)):
                s2 += dic[S2[len(S2)-1-i]]*(10**i)
            for i in range(len(S3)):
                s3 += dic[S3[len(S3)-1-i]]*(10**i)

            if s1 + s2 == s3:
                print(s1)
                print(s2)
                print(s3)
                flag == True
                return
    if flag == False:
        print(ERROR)



if __name__ == '__main__':
    main()
