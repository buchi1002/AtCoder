A, B, C, D = map(int, input().split())

width = C-A
height = D-B


S = (width//4)*(height//2)*8

left = A%4
bottom = B%2

if A%4 == 0:
    if B%2 == 0:
        S += 2 + 4*(width//4) + 3*(height//2)
    else:
        S += 3 + 8*(width//4) + 3*(height//2)
elif A%4 == 1:
    if B%2 == 0:
        S += 3 + 4*(width//4) + 6*(height//2)
    else:
        S += 6 + 8*(width//4) + 6*(height//2)
elif A%4 == 2:
    if B%2 == 0:
        S += 3 + 4*(width//4) + 7*(height//2)
    else:
        S += 7 + 8*(width//4) + 7*(height//2)
elif A%4 == 3:
    if B%2 == 0:
        S += 3 + 4*(width//4) + 7*(height//2)
    else:
        S += 7 + 8*(width//4) + 7*(height//2)
