# Write a program to count the number of sentences, words and characters 
# in a give page of text

from sys import argv

def sentence(test):
    with open(test, 'r') as file1:
        words = file1.read()
        
    return words.count('.')

def words(test):
    with open(test, 'r') as file2:
        words = file2.read().strip().split()
    words_count = len(words)
    
    return words_count  

def characters(test):
    count = 0
    with open(test, 'r') as file3:
        words = file3.read().strip().split()
    for word in words:
        for char in word:
            count += 1
        
    return count


script, test = argv
print("No of sentences in the file is: ", sentence(test))

print("No of words in the file is: ", words(test))

print("No of characters in the file is: ", characters(test))