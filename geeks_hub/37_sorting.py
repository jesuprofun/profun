# Write a program to sort list of numbers without using built-in functions

def ascending(lyst):
    
    for i in range(len(lyst)):
        for j in range(length):
            if lyst[i] < lyst[j]:
                lyst[i], lyst[j] = lyst[j], lyst[i]
    
    return lyst

lyst = [2,34,6,5,23,56,57,6,23]

ans = ascending(lyst)
print(ans)