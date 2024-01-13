from bisect import bisect_right
def main():
    N, Q = map(int, input().split())
    Rs = list(map(int, input().split()))
    Rs.sort()
    Ss = [0]*N
    Ss[0] = Rs[0]
    for i in range(1, N):
       Ss[i] = Ss[i-1] + Rs[i]

    for _ in range(Q):
      X = int(input())

      print(bisect_right(Ss, X))


main()
