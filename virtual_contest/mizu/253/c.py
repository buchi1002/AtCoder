import math
def main():
    R, X, Y = map(int, input().split())

    d = X**2 + Y**2
    k = 0
    while ((k+1)**2)*(R**2) <= d:
        k += 1

    if k == 0:
        print(2)
    elif (k**2)*(R**2) == d:
        print(k)
    else:
        print(k+1)
if __name__ == '__main__':
    main()
