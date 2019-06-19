
def fib(num):

    a = 1
    b = 1

    for i in range(num):
        print(a, end=' ')
        c = a + b
        a = b
        b = c
    print()


num = int(input("Enter the number: "))
fib(num)