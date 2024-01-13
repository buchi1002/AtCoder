def main():
    B, G = map(int, input().split())
    if B == max(B, G):
        print("Bat")
    else:
        print("Glove")

main()
