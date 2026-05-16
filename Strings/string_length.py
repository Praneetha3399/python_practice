# Find length without using len()

message = "Hello, World!"
length = 0

for char in message:
    length += 1

print(f"Length of the string: {length}")