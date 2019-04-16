from math import sqrt


c = 50
h = 30
value = []
nums = [x for x in input("Enter the numbers:").split(',')]
for d in nums:
    value.append(str(int(sqrt((2 * c * int(d))/h))))
print(','.join(value))
