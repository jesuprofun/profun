
# Bubble sort
lyst = [123, 4, 23, 3, 57, 34, 45, 7, 4, 567, 56]
length = len(lyst)
for i in range(length):
    for j in range(i):
        if lyst[i] < lyst[j]:
            temp = lyst[i]
            lyst[i] = lyst[j]
            lyst[j] = temp
print(lyst)