def main():
    N, Q = map(int,input().split())
    S = set()

    for _  in range(Q):
        T, A, B = map(int,input().split())

        if T == 1:
            S.add((A,B))
        elif T == 2:
            S.discard((A,B))
        else:
            if (A, B) in S and (B, A) in S:
                print("Yes")
            else:
                print("No")

main()
