
def oddeven(numbers):
    odd = []
    even = []
    for i in numbers:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    even.sort()
    odd.sort()
    print("Even numbers in the list are: ",even)
    print("Odd numbers in the list are: ",odd)
    for i in even:
        odd.append(i)
    print("Required list is : ",odd)



x = int(input("Enter the number of elements:"))
total = []
for i in range(x):
    y = int(input("Enter the numbers:"))
    total.append(y)
print(total)
oddeven(total)