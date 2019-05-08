# def fn(n):
#     return lambda x: x + n
#
#
# f = fn(42)
# print(f)
# print(f(0))
# print(f(1))


def f(a):
    multiplier = 2
    return a * multiplier


b = 10
c = f(b)
print(c)
print(c(10))
