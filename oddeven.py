

def mainlist(total):
    even = []
    odd = []
    for i in total:
        if (i % 2 == 0):
            even.append(i)

        else:
            odd.append(i)

    print("\nThe Even numbers in the list are:", even, end=" ")
    print("\nThe Odd numbers in the list are:", odd, end=" ")




x = int(input("Enter the number of elements:"))
total = []
for i in range(x):
    y = int(input("enter the number:"))
    total.append(y)
print(total)
mainlist(total)