# Write a lambda to check whether or not given number is multiple of 3 and multiple of 7

num = int(input("Enter a number: "))
check = lambda num : True if num % 3 == 0 and num % 7 == 0 else False
result = check(num)
if result == True:
    print("The number is  multiple of 3 and multiple of 7")
else:
    print("The number is  not multiple of 3 and multiple of 7")
