# For a list that has numbers, find the sum of odd numbers and the sum of even numbers

def odd_even(lyst):
    odds = []
    evens = []
    for i in lyst:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)

    return odds, evens

def add(lyst):

    sum = 0
    for i in lyst:
        sum = sum + i
    return sum

lyst = [2,2,35,46,456,32,31,21,4,354,65,24,5,4,2,23]

odds, evens = odd_even(lyst)
print("Sum of odd numbers in the list is : ", add(odds))
print("Sum of even numbers in the list is : ", add(evens))