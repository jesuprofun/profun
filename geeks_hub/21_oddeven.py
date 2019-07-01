# Write a program in Python that takes a list and returns two lists - odd and even lists 
# such that the odd list contains a list of all odd numbers even lists contains a 
# list of all even numbers

def odd_even(lyst):
    odds = []
    evens = []
    for i in lyst:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)

    return odds, evens


lyst = [2,2,35,46,456,32,31,21,4,354,65,24,5,4,2,23]

odds, evens = odd_even(lyst)

print("Odd list is -> ", odds)
print("Even list is -> ", evens)