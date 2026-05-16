# Count duplicate characters in a string

message = "Hello, World!"
char_count = {}
for char in message:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

duplicates = {char: count for char, count 
              in char_count.items() 
              if count > 1}

print(f"Duplicate characters: {duplicates}")


