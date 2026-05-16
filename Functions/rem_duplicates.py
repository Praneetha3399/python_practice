def remove_duplicates(message):

    duplicates = ""

    for char in message:
        if char not in duplicates:
            duplicates += char

    return duplicates 

result = remove_duplicates("programming")

print(result)