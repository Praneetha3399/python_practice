# Lists

item = [1,2,3]

item.insert(1,100)

print(item)

# Get even numbers

def get_even_numbers(numbers):

    even_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

result = get_even_numbers([1,2,3,4,5,6])

print(result)

# Count char

def count_characters(message):

    count = {}

    for char in message:
        if char in count:
            count[char] +=1
        else:
            count[char] = 1
    return count

result2 = count_characters("hello")

print(result2)