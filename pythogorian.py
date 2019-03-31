
def pythogoras(n1,n2,n3):
    import math
    if (pow(n1,2) + pow(n2,2) == pow(n3,2)):
        print("Pythogoras numbers")
    else:
        print("Not Pythogoras numbers")


n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))
n3 = int(input("Enter the third number:"))
numbers = [n1,n2,n3]
numbers.sort()
print(numbers)
a = numbers[0]
b = numbers[1]
c = numbers[2]
pythogoras(a,b,c)
