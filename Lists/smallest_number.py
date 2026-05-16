# Find smallest number in list

numbers = [10,20,5,40]

small_num = numbers[0]

for number in numbers:
    if number < small_num:
        small_num = number

print(small_num)