
def f(*args, **kwargs):
    print(args, kwargs)

print(f())
print(f(1, 2, 3))
print(f(a=1, b=2, c=3))