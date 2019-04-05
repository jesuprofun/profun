
class Animals:
    def __init__(self, colour, size):
        self.colour = colour
        self.size = size

    def bark(self):
        print("WOW WOW")


sony = Animals("brown", "small")
print(sony.colour)
sony.bark()
