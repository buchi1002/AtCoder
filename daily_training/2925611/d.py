X, Y, Z = map(int, input().split())


if X < 0:
    X, Y, Z = -X, -Y, -Z

if X < Y or Y < 0:
    print(X)
else:
    if Z < Y:
        if 0 < Z:
            print(X)
        else:
            print(-Z * 2 + X)
    else:
        print(-1)
