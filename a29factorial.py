
def factorial(m):
    n = 1
    if m > 0:
        for i in range(m,1,-1):
            n *= i
    print(n)



a = int(input("Enter the number: "))
factorial(a)

