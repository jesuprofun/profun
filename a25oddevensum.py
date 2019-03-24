
def add(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum

def oddeven(z):
    odd = []
    even = []
    for i in z:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    print("Even numbers in the list are:",even)
    print("Odd numbers in the list are:", odd)
    a = add(even)
    print("Sum of even numbers are:",a)
    b = add(odd)
    print("Sum of odd numbers are:",b)


x = int(input("Enter the number of elements: "))
z = []
for i in range(x):
    y = int(input("Enter the number: "))
    z.append(y)
print(z)
oddeven(z)