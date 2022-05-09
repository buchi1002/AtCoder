def main():
    x = input()
    X1 = int(x[0])
    X2 = int(x[1])
    X3 = int(x[2])
    X4 = int(x[3])
    if (X2 == X1 + 1) or (X2 == 0 and X1 == 9):
        if (X3 == X2 + 1) or (X3 == 0 and X2 == 9):
            if (X4 == X3 + 1) or (X4 == 0 and X3 == 9):
                print("Weak")
            else:
                print("Strong")
        else:
            print("Strong")
    elif (X1 == X2 and X2 == X3 and X3 == X4):
        print("Weak")
    else:
        print("Strong")
if __name__ == '__main__':
    main()
