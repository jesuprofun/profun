# Write a program to sort a list in descending order

def descending(lyst):
    length = len(lyst)
    for i in range(length):
        for j in range(length):
            if lyst[i] > lyst[j]:
                lyst[i], lyst[j] = lyst[j], lyst[i]
    
    return lyst

lyst = [2,34,6,5,23,56,57,6,23]

ans = descending(lyst)
print(ans)
