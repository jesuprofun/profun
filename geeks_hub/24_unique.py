# Write a program to find the number of unique numbers in the list

def unique(lyst):

    new_lyst = []
    for i in lyst:
        if i not in new_lyst:
            new_lyst.append(i)

    return new_lyst

lyst = [10, 20, 10, 30, 40, 40] 

ans = unique(lyst)
print("Unique numbers in the list are : ", end = " ")
for i in ans:
    print(i, end = " ")
print()
    