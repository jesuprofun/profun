
lyst = [16, 17, 4, 3, 5, 2]
count = len(lyst)


for i in range(0, count):
    for j in range(i+1, count):
        if lyst[i] <= lyst[j]:
            break
    if j == count - 1:
        print(lyst[i])