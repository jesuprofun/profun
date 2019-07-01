# Write a program to find the largest number in the list.

def largest(lyst):
     
    big = 0
    for i in lyst:
        if i > big:
            big = i

    return big

lyst = [123,25,34,2,3,4,365,3,2,345,23]

print("Largest number in the list is", largest(lyst))
