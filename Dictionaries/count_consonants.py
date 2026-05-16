# count consonants in a string
message = "Hello, World!"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
consonants_count = {}

for char in message:
    if char in consonants:
        if char in consonants_count:
            consonants_count[char] += 1
        else:
            consonants_count[char] = 1
print(f"Consonant counts: {consonants_count}")

# Count consonants in a string

consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
consonant_count = 0

for char in message:
    if char in consonants:
        consonant_count += 1

print(f"Number of consonants: {consonant_count}")


# find the duplicate consonants in a string
duplicates = {}

for char, count in consonants_count.items():
    if count > 1:
        duplicates[char] = count

print("Consonant count more than once:", duplicates)



