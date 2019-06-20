class Complex:

    x = 2
    y = 3

    def printc(self, x, y):
        print(x, y)

    def cmod(self, x, y):
        print(x * x + y * y)


c1 = Complex()
c1.printc(c1.x, c1.y)
c1.cmod(c1.x, c1.y)