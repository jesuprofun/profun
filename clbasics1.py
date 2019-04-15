
class Animals:
    def __init__(self, colour, legs):
        self.colour = colour
        self.legs = legs

    class Cat(Animals):
        def meow(self):
            print("meow")

    class Dog(Animals):
        def wow(self):
            print("wow")


sony = Dog("Brown",4)
pussy = Cat("White",4)
print(sony.colour)
print(sony.legs)
print(pussy.colour)
print(pussy.legs)
