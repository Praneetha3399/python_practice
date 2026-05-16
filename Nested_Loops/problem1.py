numbers = [1,2,3]

for number1 in numbers:
    for number2 in numbers:
        print(number1, number2)

for row in range(1,5):
    for col in range(1, row +1):
        print("*", end = " ")
    print()