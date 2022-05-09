def main():
    L = {"ABC", "ARC", "AGC", "AHC"}

    for i in range(3):
        S = input()
        if S in L:
            L.remove(S)
    for i in L:
        print(i)
if __name__ == '__main__':
    main()
