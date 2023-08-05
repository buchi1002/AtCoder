def main():
    N = int(input())

    Bs = [soeted(map(int, input().split()), key = lambda x: -x) for _ in range(N)]

    Bs.sort(key = lambda x: -x[0])
