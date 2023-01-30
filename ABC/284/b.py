def main():

    T = int(input())

    for _ in range(T):
        N = int(input())
        As = list(map(int,input().split()))

        count = 0
        for i in range(N):
            if As[i]%2 == 1:
                count += 1

        print(count)
main()
