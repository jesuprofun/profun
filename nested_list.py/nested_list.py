
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8], 
    [9, 10, 11, 12]
]

transposed = []

for i in range(4):
    sublist = []
    for row in matrix:
        sublist.append(row[i])
    transposed.append(sublist)

print(transposed)