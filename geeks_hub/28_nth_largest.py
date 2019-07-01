# Given a number “N” and a list that has numbers, 
# write a program to find the Nth largest element in the list

def largest_nth(n, lyst):
    return lyst[n-1]

def descending(lyst):

    for i in range(len(lyst)):
        for j in range(len(lyst)):
            if lyst[i] > lyst[j]:
                lyst[i], lyst[j] = lyst[j], lyst[i]

    return lyst


lyst = [23, 23, 5, 23, 2, 6, 2, 5, 78]


ordered_lyst = descending(lyst)
n = int(input("Enter the value for n: "))
print("nth largest number in the list is: ", largest_nth(n, ordered_lyst))
