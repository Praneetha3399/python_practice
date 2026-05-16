def reverse_string(message):

    rev_string = ""

    for char in message:
        rev_string = char + rev_string
    return rev_string

result = reverse_string("python")

print(result)