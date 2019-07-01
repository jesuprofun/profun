# Write a program to find whether the given string is a palindrome or not

def rev(string):
    return string[::-1]

def is_palindrome(string):

    reverse = rev(string)
    if string == reverse:
        return True
    else:
        return False

    
string = input("Enter the string: ")
ans = is_palindrome(string)

if ans:
    print("Palindrome")
else:
    print("Not Palindrome")