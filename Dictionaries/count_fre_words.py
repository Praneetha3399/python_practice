# Count frequency of each word

string = "hello world hello"

word_list = {}

for word in string.split():
    if word in word_list:
        word_list[word] += 1
    else:
        word_list[word] = 1


print(word_list)