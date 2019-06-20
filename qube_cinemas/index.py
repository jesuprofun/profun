
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
    with open('index.txt', 'w') as file1:
        for k,v in index.items():
            file1.write(str(k) + ' is contained '+ str(v) + '\n' )
    
    

lyst1 = read_file('new_1.txt')
indexed = indexing(index, lyst1, 'new_1.txt')


lyst2 = read_file('new_2.txt')
indexed2 = indexing(indexed, lyst2, 'new_2.txt')
print(indexed2)

lyst3 = read_file('new_3.txt')
indexed3 = indexing(indexed2, lyst3, 'new_3.txt')
print(indexed3)

write_file(indexed3)

