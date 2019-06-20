# function to arrange largest numbers in reverse order
def largest(numbers):
    numbers.sort()
    numbers.reverse()
    return numbers

# to find Nth largest number
def find(n,large):
    m = len(large)
    if n < m:
        return large[n]
    else:
        return None


# Getting numbers for the list
x = int(input("Enter the number of elements: "))
total = []
for i in range(x):
    y = int(input("Enter the numbers: "))
    total.append(y)
print("The numbers in the list are: ",total)
large = largest(total)
print("Largest to smallest",large)
#Getting the N number
n = int(input("Enter the N number: "))
nlarge = find(n,large)
print(nlarge)
