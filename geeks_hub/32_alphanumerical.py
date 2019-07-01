# Write a program that accepts a sequence of whitespace separated words as input and 
# prints the words after removing all duplicate words and sorting them alphanumerically.

def alphanumerical(Words):
    lyst = []
    words.sort()
    for word in words:
        if word not in lyst:
            lyst.append(word)
    print(lyst)


words = input("Enter the string: ").split(' ')
alphanumerical(words)