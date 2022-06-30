xa,ya,xb,yb,xc,yc = map(int,input().split())
X1, X2 = xb - xa, xc - xa
Y1, Y2 = yb - ya, yc - ya

print(abs(X1*Y2-X2*Y1)*(1/2))
