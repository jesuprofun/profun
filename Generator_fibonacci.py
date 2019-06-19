
def fib_gen(limit):

    a, b = 0, 1

    while a < limit:
        yield a

        a, b = b, a+b

    
x = fib_gen(6)

print(next(x))
print(next(x))
print(next(x))
print(next(x))  