
func1 = lambda x: x ** 2
print(func1(3))

# func2 = lambda x, y: x + y
# func2(2, 3)

def apply_func(fn, *args):
    return fn(*args)

print(apply_func(func1,3))
