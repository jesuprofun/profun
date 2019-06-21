
index = {}
def read_file(file):

    with open(file, 'r') as file1:
        words = file1.read().strip().split()
    
    return words

def indexing(index, lyst, file_name):

    
    count = 1

    for word in lyst:
        if word not in index:
            index[word] = {}
            index[word][file_name] = count
        elif file_name not in index[word]:
            index[word][file_name] = count
        else:
            index[word][file_name] += 1  
        
    return index

def write_file(index):
    import json

    with open('index.txt', 'w') as file1:
        json.dump(index, file1)    
    
from sys import argv

file_lyst = argv[1:]

for file in file_lyst:
    file_input = read_file(file)
    index = indexing(index, file_input, file)

print(index)

write_file(index)
