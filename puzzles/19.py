# 2nd largest among 3 numbers

numbers = list(map(int, input("Enter 3 numbers with comma:").split(',')))
numbers.sort()
print("{} is the 2nd largest number".format(numbers[-2]))