def main():
    N, M = map(int, input().split())
    G = [list() for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    Ps = set()
    d_dic = dict()
    K = int(input())
    for k in range(K):
        p, d = map(int, input().split())
        Ps.add(p-1)
        d_dic[p-1] = d

    Bs = [False]*N
    clear = set()
    for i in range(N):
        Flag = True
        cand_clear = set()
        C1 = set([i])
        seen = [False for _ in range(N)]
        seen[i] = True
        distance = 0
        while len(C1) != 0:
            C2 = set()
            for k in C1:
                if k in Ps:
                    if distance == d_dic[k]:
                        cand_clear.add(k)
                    elif distance < d_dic[k]:
                        Flag = False
                        break

                for c in G[k]:
                    if not seen[c]:
                        seen[c] = True
                        C2.add(c)


            if not Flag:
                break
            C1, C2 = C2, C1
            distance += 1


        if Flag:
            Bs[i] = True
            clear |= cand_clear

    if len(clear) == K:
        s = ""
        for i in range(N):
            if Bs[i]:
                s += "1"
            else:
                s += "0"
        print("Yes")
        print(s)
    else:
        print("No")


main()
