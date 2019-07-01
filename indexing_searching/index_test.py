
from sys import argv


def read_file(file):
    """ Function to read file and to return the words in a list """

    with open(file, 'r') as file1:

        words = file1.read().strip().split()
    
    return words 


def create_index(index, words, file_name):
    """ Function to create index with arguments index as dictionary,
        words from the file and the file name """
    
    count = 0
    for word in words:
        
        if word not in index:
            # Initially the nested dictionary is created for each word in words as key
            # and file_name with count as value
            index[word] = {}
            index[word][file_name] = 1
            index[word]['position'] = [count]
        elif file_name not in index[word]:
            # To update the file_name
            index[word][file_name] = 1
        else:
            # To update the count
            index[word][file_name] += 1 
            index[word]['position'].append(count)  
        count += 1

    return index


def write_file(index):
    """The nested dictionary is then converted to json format and 
        then it is written to the index_text file """
    import json

    index_text = 'index.txt'
    with open(index_text, 'w') as file1:
        json.dump(index, file1)    


def main():
    """The main function to get the text file passed in as the argument, 
        the words are indexed and written in a new file """
    file_lyst = argv[1:]
    index = {}

    for file in file_lyst:
        # Reads the file and convert it into words
        file_input = read_file(file)
        # Indexing the words 
        index = create_index(index, file_input, file)
    
    # The indexed content is written in the index file from the same folder
    write_file(index)

    print(index)


main()


