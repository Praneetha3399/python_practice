# 

message = "swiss"
duplicates = {}

for char in message:
    if char in duplicates:
        duplicates[char] += 1
    else:
        duplicates[char] = 1

print(duplicates)

reversed_message = message[::-1]
for char in reversed_message:
    if duplicates[char] == 1:
        print ("First non-repeating character:", char)
        break