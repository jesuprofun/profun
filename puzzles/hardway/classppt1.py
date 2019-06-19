class Complex:

    def __init__(self, x, y):
        self.real = x
        self.imag = y

    def printc(self):
        print(self.real, self.imag)


c1 = Complex(1.0, 2.0)
c2 = Complex(3.0, 4.0)

# c1.printc()
# c2.printc()

print(Complex.printc)
print(c1.printc)