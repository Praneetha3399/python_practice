try:
    print(5/0)

except:
    print("Cannot divide by zero")

try:

    numbers = [1,2,3]
    print(numbers[5])

except Exception as e:
    print(e)

finally:
    print("Execution Completed")