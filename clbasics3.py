
class Car:

    light = 3

    def __init__(self):
        self.make = "AUDI"
        self.wheels = 4

c1 = Car()
c2 = Car()

print(c1.make, c1.wheels, Car.light)
print(c2.make, c2.wheels, Car.light)