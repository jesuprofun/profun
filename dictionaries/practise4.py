

lyst  = [2, 4 ,6, 7, 3, 1]

count = 0 
big = lyst[0]
while count == 0:
    for i in range(len(lyst)):
        if lyst[i] > big:
            big = lyst[i]
    count -= 1

print(big)