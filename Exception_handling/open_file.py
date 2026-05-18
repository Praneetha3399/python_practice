try:
    file = open("abc.txt")
    file.close()
except Exception as e:
    print(e)


try:
    print(10/2)

finally:
    print("Program ended")

