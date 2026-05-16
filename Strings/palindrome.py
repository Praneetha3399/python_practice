# Check if a string is a palindrome

message = "madam"
if message == message[::-1]:
    print(f"{message} is a palindrome")
else:
    print(f"{message} is not a palindrome")

# Check if a string is a palindrome without slicing

message = "madam"
reversed_message = ""
for char in message:
    reversed_message = char + reversed_message  
if message == reversed_message:
    print(f"{message} is a palindrome")
else:
    print(f"{message} is not a palindrome")