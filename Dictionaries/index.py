message = "swiss"

count = {}

for char in message:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1 

print(count)

# index of first non-repeating character

for char in message:
    if count[char] == 1:
        print("All non-repeating characters:", char)
        continue

for index, char in enumerate(message):
    if count[char] == 1:
        print(f"Index of first non-repeating character: {char} is {index}")
        break   



# 
