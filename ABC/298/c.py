import bisect

def main():
    N = int(input())
    Q = int(input())
    box = [list() for i in range(N)]
    card = [list() for i in range(2*(10**5))]
    card_set = [set() for i in range(2*(10**5))]

    for i in range(Q):
        q = input()
        if q[0] == "1":
            _ , i, j = map(int, q.split())
            bisect.insort_right(box[j-1], i)

            if j not in card_set[i-1]:
                card_set[i-1].add(j)
                bisect.insort_right(card[i-1], j)

        elif q[0] == "2":
            _, i = map(int, q.split())
            print(*box[i-1])

        else:
            _, i = map(int, q.split())
            print(*card[i-1])


main()
