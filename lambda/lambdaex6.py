# Write a lambda to check whether or not given string is a palindrome

# def is_palindrome(x):
#     if x.lower() == x[::-1]:
#         return True
#     else:
#         return False
#
#
lyst = ['pop', 'profun', 'steffy', 'dad']
is_palindrome = lambda x : True if x.lower() == x[::-1] else False
for i in lyst:
    print(is_palindrome(i))

# x = 'PROFUN'
# y = x.lower()
# z = x[::-1]
# print(y)
# print(z)
