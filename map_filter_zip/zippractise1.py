
l1 = [1, 2, 3, 4, 5, 6]
l2 = [10, 20, 30, 40, 50, 60]
l3 = [100, 200, 300, 400, 500, 600]

res = zip(l1, l2, l3)
# print(list(res))

# for i in res:
#     print(i)

for a, b, c in res:
    print(a,b,c)
