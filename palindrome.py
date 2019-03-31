
def reverse(str):
    return str[::-1]
def ispalindrome(str):
    rev = reverse(str)
    if str == rev:
        return True
    else:
        return False



str = input("Enter a string: ")
x = ispalindrome(str)

if x == True:
    print ('Palindrome')
else:
    print("Not a Palindrome")


