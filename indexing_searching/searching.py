
from sys import argv

def read_file(text_file):
    """ Function to load json file"""
    import json 

    with open(text_file, 'r') as file1:
        datas = json.load(file1)
    
    return datas


def search_string(datas, words):
    """ FUnction to scan the indexe file for the words passed in the command line"""
    for word in words:
        for key in datas:
            if key == word:    
                print("Searching for", word)
                print('     found in ')
                for value in datas[key]:
                    print('\t' + value)
                print()


def conditional_search(datas, words):
    """ Function to support Conditional Searching"""
    word_1 = []
    word_2 = []
   # Search for words in file and updates the list with the file_name 
    for key, value in datas.items():
        if key == words[0]:
            for inner_k in value:
                word_1.append(inner_k)
        elif key == words[2]:
            for inner_k in value:
                word_2.append(inner_k)
    # print(word_1)
    # print(word_2)

    # Returns a list for conditional searching
    search_result = []
    for word in word_1:
        if word in word_2 and word not in search_result:
            search_result.append(word)

    return search_result


def main():
    """ The main function to get input words passed in the command line 
        and to search the word in the index file""" 

    # File input from the command line argument
    text_file = argv[1]
    datas = read_file(text_file)

    # Searches and displays the words in the file 
    words = argv[2:]
    search_string(datas, words)
    
    # Conditional search
    input_words = list(input("Enter Words for conditional searching: ").split())
    search_result = conditional_search(datas, input_words)
    print(search_result)
    
main()