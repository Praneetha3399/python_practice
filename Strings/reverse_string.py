# Reverse a string

message = "Hello, World!"
reversed_message = message[::-1]
print(reversed_message)


string = "hello"

rev_string = ""

for char in string:
    rev_string = char + rev_string

print(rev_string)