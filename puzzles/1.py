
lyst = []
for i in range(2000,3200):
    if i % 7 == 0 and i % 5 != 0:
        lyst.append(str(i))
print(','.join(lyst))
