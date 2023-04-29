from collections import deque

def main():
    Q = int(input())
    mod = 998244353

    deq = deque([1])
    v = 1
    for i in range(Q):
        q = input()
        if q[0] =="1":
            _, x = map(int, q.split())
            deq.append(x)
            v = (v*10 + x)%mod
        elif q[0] == "2":
            y = deq.popleft()
            v = (v - y*pow(10, len(deq), mod))%mod
        else:
            print(v)



main()
