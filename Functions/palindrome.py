def is_palindrome(message):

    rev_string = "" 

    for char in message:
        rev_string = char + rev_string
    
    return message == rev_string
    
result = is_palindrome("madam")

print(result)