
def str_len(str1, str2):  

    if len(str1) > len(str2):
        print(str1)
    elif len(str1) < len(str2):
        print(str2)
    else:
        for i in str1, str2:
            print(i)
    

str1, str2 = map(str, input("Enter two strings with comma: ").split(','))
str_len(str1, str2)