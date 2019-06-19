# Given list
lyst = [5, 8, 2, 3, 7, 6]

# First we will find the largest number
big = lyst[0]
for i in range(1, len(lyst)):
    if lyst[i] > big:
        big = lyst[i]
m1 = big

# TO find second largest
m2 = -9999999

for i in lyst:
    if i != m1 and i > m2:
        m2 = i
print(m2)