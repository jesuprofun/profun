
def sum(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b

mem = []
while True:
    if len(mem) < 6:
        print("1.Addition \n2.Subtraction\n3.Multiplication\n4.Division\n5.Clear memory")
        choice = int(input("Enter your choice: "))
        if choice <= 4:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
        if choice == 1:
            ans = sum(num1, num2)
            print("Sum of two numbers is", ans)
            mem.append(ans)
        elif choice == 2:
            ans = sub(num1, num2)
            print("Difference of two numbers is", ans)
            mem.append(ans)
        elif choice == 3:
            ans = mul(num1, num2)
            print("Product of two numbers is", ans)
            mem.append(ans)
        elif choice == 4:
            ans = div(num1, num2)
            print("Division of two numbers is", ans)
            mem.append(ans)
        elif choice == 5:
            mem.clear()
            print("Memory Cleared ",mem)
        else:
            print("Invalid input")


    else:
        del mem[0]

    print("Memory : ",mem)
