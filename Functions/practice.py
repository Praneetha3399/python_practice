# reverse_string(message)

def reverse_string(message):

    rev_string = ""

    for char in message:
        rev_string = char + rev_string
    
    return rev_string

result = reverse_string("hello")

print(result)

#  is_palindrome(message)

def is_palindrome(message):

    rev_string = ""

    for char in message:
        rev_string = char + rev_string
    
    return rev_string == message

result = is_palindrome("madam")

print(result)

#  count_vowels(message)

def count_vowels(message):

    vowels = "aeiou"

    count = 0

    for char in message:
        if char in vowels:
            count +=1

    return count

result = count_vowels("Automation")

print(result)

# remove_duplicates(message)

def remove_duplicates(message):

    rem_dup = "" 

    for char in message:
        if char not in rem_dup:
            rem_dup += char

    return rem_dup

result = remove_duplicates("programming")

print(result)

# char_frequency(message)

def char_frequency(message):

    dup = {}

    for char in message:
        if char in dup:
            dup[char] +=1
        else:
            dup[char] = 1

    return dup

result = char_frequency("aabbccddd")

print(result)

#  get_even_numbers(numbers)

def get_even_numbers(numbers):

    even_num = []

    for num in numbers:
        if num % 2 == 0:
            even_num.append(num)

    return even_num

result = get_even_numbers([1,2,3,4,5,6])

print(result)

#  find_largest(a,b)

def find_largest(a,b):

    if a>b:
        return a
    else:
        return b
    
result = find_largest(3,4)

print(result)

