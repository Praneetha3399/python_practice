# Count vowels in a string

message = "Hello, World!"
vowels = "aeiouAEIOU"
count = 0

for char in message:
    if char in vowels:
        count += 1

print(f"Number of vowels: {count}")


# count the number of vowels in a string
vowel_count = {}

for char in message:
    if char in vowels:
        if char in vowel_count:
            vowel_count[char] += 1
        else:
            vowel_count[char] = 1

print(f"Vowel counts: {vowel_count}")


# Count all 5 vowels in a string

found = set()

for char in message:
    if char in vowels:
        found.add(char)

print(f"Vowels found: {found}")