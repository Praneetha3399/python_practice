# Remove duplicates from string

message = "programming"


result = ""

for char in message:
    if char not in result:
        result += char

print(result)




