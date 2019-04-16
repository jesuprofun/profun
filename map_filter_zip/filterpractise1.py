
def is_even(x):
    return x % 2 == 0
l1 = [1, 2, 3, 4, 5, 6]
l2 = [10, 20, 30, 40, 50, 60]
l3 = [100, 200, 300, 400, 500, 600]

res = filter(is_even, l1)
print(list(res))

res1 = filter(lambda x : x % 2 == 0, l1)
print(list(res1))

l1 = [0, None, False, {}, {}, set(), tuple(), 1, True, (1, 2)]
result = filter(None, l1)
print(list(result))
