m = int(input())

if m < 100:
    print("00")
elif m <= 5000:
    print(str(m//100).zfill(2))
elif m <= 30000:
    print(str(m//1000+50).zfill(2))
elif m <= 70000:
    print(str((m//1000 -30)//5 + 80).zfill(2))
else:
    print(89)
