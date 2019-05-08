
def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)


number = int(input("Enter the number to find factorial: "))
factorial = fact(number)
print(factorial)
