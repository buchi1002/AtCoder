def main():
    N = bin(int(input()))[2:]

    L = len(N)

    S = "A"
    for i in range(1,L):
        if N[i] == "1":
            S = S + "BA"
        else:
            S = S + "B"


    print(S)
if __name__ == '__main__':
    main()
