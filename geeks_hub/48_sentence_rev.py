# Write a program in Python that reverses the words in a sentence

def reverse(sentence):

    return sentence[::-1]

sentence = input("Enter the sentence: ").split(' ')

rev_sen = reverse(sentence)
for word in rev_sen:
    print(word, end = ' ')
print()
