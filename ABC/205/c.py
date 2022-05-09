def main():
    # input
    A, B, C = map(int, input().split())
    # compute
    if(C%2 == 0):
        if(A**2 == B**2):
            print("=")
        elif(A**2 < B**2):
            print("<")
        else:
            print(">")
    else:
        if(A == B):
            print("=")
        elif(A < B):
            print("<")
        else:
            print(">")
    # output

if __name__ == '__main__':
    main()
