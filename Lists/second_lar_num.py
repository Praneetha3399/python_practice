# Second largest number

numbers = [10, 20, 5, 40, 30]

sec_number = numbers[0]

lar_number = numbers[0]

for number in numbers:
    if number > lar_number:
        lar_number = number

for number in numbers:
    if number != lar_number and number > sec_number:
        sec_number = number

print(sec_number)






    