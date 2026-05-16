def char_frequency(message):

    duplicates = {}

    for char in message:
        if char in duplicates:
            duplicates[char] +=1
        else:
            duplicates[char] =1
    return duplicates

result = char_frequency("aabbcc")

print(result)