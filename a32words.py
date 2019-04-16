# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

def lower_case(str):
    return str.lower()

def split_string(str):
    return str.split(' ')

def remove_duplicate(str):
    new_lyst = []
    for i in str:
        for j in str:
            if i == j:
                if i not in new_lyst:
                    new_lyst.append(i)
            else:
                pass
    return new_lyst

input_string = 'Python is beautiful where JAVA is not beautiful'
# print(input_string)
lower_string = lower_case(input_string)
# print(lower_string)
splitted_string = split_string(lower_string)
# print(splitted_string)
str_length = len(splitted_string)
# print(str_length)
str_dup = remove_duplicate(splitted_string)
# print(str_dup)
# Sorting alphanumerically
print(set(str_dup))
