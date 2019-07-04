
a = [[1, 4, 5, 12], 
    [-5, 8, 9 ,0],
    [-6, 7, 11, 19]]

cloumn = []
for i in range(4):
    cloumn.append([])
    for row in a:
        cloumn[i].append(row[i])

print(cloumn)