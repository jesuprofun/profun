
lyst = [x for x in input("Enter 4 bit binary nums with comma: ").split(',')]
res_lyst = []
for i in lyst:
    bin = int(i,2)
    if bin % 5 == 0:
        res_lyst.append(i)
print(','.join(res_lyst))
