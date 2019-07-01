# Given a few words, convert them to lowercase, UPPERCASE, and CamelCase. 
# Print them to the console

def upper_case(words):
    return words.upper()

def lower_case(words):
    return words.lower()

def camel_case(words):
    return words[0].upper() + words[1:].lower()


words = input("Enter the words with comma: ").split(',')
print(words)
for word in words:
    upp = upper_case(word)
    print(upp, end=" ")
print()
for word in words:
    low = lower_case(word)
    print(low, end=" ")
print()
for word in words:
    cam = camel_case(word)
    print(cam, end=" ")

print()

