
def func(*args):
    return sum(args)

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
l3 = [100, 200, 300, 400, 500, 600, 700, 800, 900]

res_lyst = list(map(func, l1, l2, l3))

print(res_lyst)

res_lyst1 = list(map(lambda x, y : x + y, l1, l2))
print(res_lyst1)

res_lyst3 = list(map(lambda *args : sum(args), l1, l2, l3))
print(res_lyst3)
