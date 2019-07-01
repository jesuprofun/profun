# Write a python function that returns first “N” Fibonacci numbers for a given “N”

def fibonacci(num):

    a, b = 0, 1

    for i in range(num):

        print(a)
        a, b = b, a + b

number = int(input("Enter the number: "))

fibonacci(number)
