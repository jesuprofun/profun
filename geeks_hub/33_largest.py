# Implement a function that takes as input three variables, and 
# returns the largest of the three.

def largest(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1

    elif num2 > num3:
        return num2
    
    else:
        return num3
    

numbers = input("Enter three numbers with space: ")
a, b, c = map(int, numbers.split(' '))
print("The largest among the three numbers is: ", largest(a, b, c))