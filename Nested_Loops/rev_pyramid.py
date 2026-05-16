for row in range(1,5):
    for col in range(2*row -1):
        print(" ", end = "")
    for star in range(4-row):
        print("*", end = "")
    print()