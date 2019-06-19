
def fact(num):
    if not isinstance(num, int) or  num < 0:
        raise ValueError("Invalid Integral")

    fact = 1
    for i in range(num, 1, -1):
        fact = fact * i

    return fact

num = int(input("Enter the number: "))

print(fact(num))