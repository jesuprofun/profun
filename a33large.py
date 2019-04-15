# Implement a function that takes as input three variables, and returns the largest of the three.

def large(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            return num1
    elif num2 > num3:
        return num2
    else:
        return num3


a = int(input("Enter three first number: "))
b = int(input("Enter three second number: "))
c = int(input("Enter three third number: "))
big_number = large(a,b,c)
print("{} is the largest of the three numbers".format(big_number))
