# largest of three numbers
a, b, c = map(int, input("Enter 3 numbers: ").split(','))
if a > b and a > c:
    print("a = {} is greater".format(a))
elif b > c:
    print("b = {} is greater".format(b))
else:
    print("c = {} is greater".format(c))