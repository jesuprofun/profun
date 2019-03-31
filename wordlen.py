
def length(str):
    a = 0
    for x in str.split():
        word_length = len(x)
        a = a + word_length
    print(a)




str = input("Enter the string: ")
length(str)
