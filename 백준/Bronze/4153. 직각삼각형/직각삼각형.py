while True:
    a, b, c = sorted(map(int, input().split()))

    if (a,b,c)==(0,0,0):
        break
    
    if a**2 + b**2 == c**2:
        print("right")
    else:
        print("wrong")

# map으로 불러올 때, sorted 해버리면 작은 순서대로 a, b, c에 들어감 !