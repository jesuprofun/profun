
matrix = [[1, 2 ,3], [4, 5], [6, 7, 8]]

# flatten_matrix = []

# for sublist in matrix:
#     for val in sublist:
#         flatten_matrix.append(j)

# print("Input matrix is ", matrix)
# print("Output matrix is", flatten_matrix)

flatten_matrix = [val for sublist in matrix for val in sublist]

print(flatten_matrix)