# Open a file in read mode and print the contents of the file line by line

# file1 = open("big.txt","r")
# contents = file1.read()
# print(contents)
# file1.close

# file2 = open("big.txt","r")
# for file in file2:
#     print(file)
# file2.close

import os

DIR = '.'
d = os.path.abspath(DIR)
print(d)