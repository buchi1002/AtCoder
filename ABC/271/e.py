from collections import defaultdict

def main():
    N, M, K = map(int,input().split())
    roads = dict()
    cost = dict()

    for i in range(N):
        a, b, c = map(int,input().split())
        roads[a] = b
        cost[tuple([a, b])] = c



if __name__ == '__main__':
    main()
