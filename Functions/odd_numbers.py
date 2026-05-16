def get_odd_numbers():

    odd_numbers = []

    for number in range(1,11):
        if number %2 == 1:
            odd_numbers.append(number)
    return odd_numbers
result = get_odd_numbers()

print(result)