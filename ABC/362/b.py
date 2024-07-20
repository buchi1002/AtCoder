x0, y0 = map(int, input().split())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

# 0
if (x1-x0)*(x2-x0)+(y1-y0)*(y2-y0)==0:
    print("Yes")
elif (x0-x1)*(x2-x1)+(y0-y1)*(y2-y1)==0:
    print('Yes')
elif (x0-x2)*(x1-x2)+(y0-y2)*(y1-y2)==0:
    print("Yes")
else:
    print('No')
