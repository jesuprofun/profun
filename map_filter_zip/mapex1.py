# Write a map to calcuate some of elements of two lists

l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30, 40, 50, 60]

res = map(lambda x ,y : x + y, l1, l2)
print(list(res))
