import math

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        v = N
        p = -1
        q = -1
        for i in range(2,N+1):
            if i*i*i >= N+5:
                break
            if v%i == 0:
                v = v//i
                if v%i == 0:
                    p = i
                    q = v//i
                else:
                    q = i
                break
        if p == -1:
            p = int(math.sqrt(v))

        print(*[p,q])
main()
