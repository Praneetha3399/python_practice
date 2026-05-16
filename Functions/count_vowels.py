def count_vowels(message):

    vowels = "aeiou"

    count = 0

    for char in message:
        if char in vowels:
            count +=1

    return count

result = count_vowels("automation")

print(result)