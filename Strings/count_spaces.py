# Count spaces in a string

message = "Hello World Python"

space_count = 0
for char in message:
    if char == " ":
        space_count += 1    
print(f"Number of spaces: {space_count}")