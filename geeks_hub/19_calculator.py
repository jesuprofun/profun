# Create a calculator covering all operations

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a // b

def printing():
    for i in range(15):
        print("*", end = " ")

lyst = []
for i in range(4):
    printing()
    print("\n       Calculator")
    printing()

    choice = int(input("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\nEnter your choice:"))

    a = int(input("\nEnter the value for a: "))
    b = int(input("Enter the value for b: "))
    if choice == 1:
        ans = add(a, b)
        print("Sum of two numbers is : ", ans)
        x = ("{} + {} = {}" .format(a, b, ans))
        lyst.append(x)

    elif choice == 2:
        ans = sub(a, b)
        print("Difference between two numbers is : ", ans)
        x = ("{} - {} = {}" .format(a, b, ans))
        lyst.append(x)

    elif choice == 3:
        ans = mul(a, b)
        print("Product of two numbers is : ", ans)
        x = ("{} * {} = {}" .format(a, b, ans))
        lyst.append(x)

    elif choice == 4:
        ans = div(a, b)
        print("Quotient of two numbers is : ", ans)
        x = ("{} / {} = {}" .format(a, b, ans))
        lyst.append(x)

    else:
        print("Wrong Choice Dude.......")

for i in lyst:
    print(i)