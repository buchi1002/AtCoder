import math
def main():
    # input
    N = int(input())
    # compute
    D = (-1 + math.sqrt(1+8*N))/2
    # output
    if D == int(D):
        print(int(D))
    else:
        print(int(D)+1)

if __name__ == '__main__':
    main()
