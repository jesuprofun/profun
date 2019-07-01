# Greatest of three numbers

# The three numbers are num1, num2 and num3
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

""" Checking for condition with if statement 
    Conditional Statement 'and' is used
    if (num1 > num2) is True and (num1 > num3) is True  
    only if both statements aree True BLock-1 will be executed
    else + if = elif
    """

# if True block-1 will be executed 
# if False block-2 will be executed 
if num1 > num2 and num1 > num3:
    # Block-1
    print("num1 = ",num1, ",is greater num2 and num3")
elif num2 > num3:
    # Block-2
    print("num2 = ",num2, ",is greater num1 and num3")
else:
    # Block-3
    print("num3 = ",num3, ",is greater num1 and num2")