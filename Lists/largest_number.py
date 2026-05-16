# Find largest number in list

numbers = [10,20,5,40]

lar_num = numbers[0]

for number in numbers:
    if number > lar_num:
        lar_num = number
        
print(lar_num)