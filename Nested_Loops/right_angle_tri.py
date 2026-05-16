for row in range(1,5):
    for col in range(4 - row):
        print(" ", end ="")
    for star in range(row):
        print("*", end = "")
    print()