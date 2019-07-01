# Biggest of two numbers

# The two numbers are num1 and num2
# I'm converting the numbers to integer with int() function
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Checking for condition with if statement 
# Comparison operator '>' returns True or False

# if True block-1 will be executed 
# if False block-2 will be executed 
if num1 > num2:
    # block-1
    print("num1 = ",num1, ",is greater") 
else:
    # block-2
    print("num2 = ",num2, ",is greater")