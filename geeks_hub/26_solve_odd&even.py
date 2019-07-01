# A list has numbers. Write a program to move odd number to start of the list and 
# even number to the end of the list. For example, the list [1,2,3,4,5,6,7,8,9,10] 
# should be transformed to [1,3,5,7,9,2,4,6,8,10]

def odd_even(lyst):
    odds = []
    evens = []
    for i in lyst:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)

    return odds + evens

lyst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(odd_even(lyst))