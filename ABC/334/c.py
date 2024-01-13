from collections import deque
def main():
    N, K = map(int, input().split())
    socks = deque(map(int, input().split()))

    ans = 0

    while len(socks) >= 2:
        if abs(socks[-1]-socks[-2]) <= abs(socks[0]-socks[1]):
            s1 = socks.pop()
            s2 = socks.pop()

        else:
            s1 = socks.popleft()
            s2 = socks.popleft()

        ans += abs(s1-s2)
    print(ans)






main()
