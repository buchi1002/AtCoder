from collections import defaultdict
def main():
    d = defaultdict(lambda:False)
    for c2x in range(-7, 7+1):
        for c2y in range(-7, 7+1):
            for c2z in range(0, -7-1, -1):
                for c3x in range(-7, 7+1):
                    for c3y in range(-7, 7+1):
                        for c3z in range(7+1):
                            V = [0, 0, 0, 0]
                            for x in range(-7, 7+1):
                                for y in range(-7, 7+1):
                                    for z in range(-7, 7+1):
                                        cnt = 0
                                        if (c2x <= x < c2x +7) and (c2y <= y < c2y + 7) and (c2z <= z < c2z + 7):
                                            cnt += 1
                                        if (c3x <= x < c3x +7) and (c3y <= y < c2y + 7) and (c3z <= z < c3z + 7):
                                            cnt += 1
                                        if (0 <= x < 7) and (0 <= y < 7) and (0 <= z < 7):
                                            cnt += 1
                                        V[cnt] += 1
                            d[tuple(V)] = (0, 0, 0, c2x, c2y, c2z, c3x, c3y, c3z)
    V = tuple(map(int, input().split()))
    if d[V]:
        print("Yes")
        print(*d[V])
    else:
        print("No")



main()
