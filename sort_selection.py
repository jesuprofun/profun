
# selection sorting
lyst = [5, 3, 8, 6, 7, 2]

length = len(lyst)

for i in range(5):
    minpos = i
    for j in range(i, 6):
        if lyst[minpos] > lyst[j]:
            minpos = j

    temp = lyst[i]
    lyst[i] = lyst[minpos]
    lyst[minpos] = temp

print(lyst)
