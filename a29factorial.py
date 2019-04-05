

def factorial(m):
    n = 1
    if m > 0:
        for i in range(m,1,-1):
            n *= i
    print(n)



number = int(input("Enter the number: "))
factorial(number)

