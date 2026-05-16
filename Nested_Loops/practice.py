list1 = [1,2,3,4]
list2 = [3,4,5,6]
count = 0
for item1 in list1:
    for item2 in list2:
        if item1 == item2:
            count +=1
print(count)