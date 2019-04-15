
class Animals:

    def __init__(self, animals1, animals2):
        self.animals1 = animals1
        self.animals2 = animals2


class Cat(Animals):

    def meow(self):
        print("Meow")


class Dog(Animals):

    def wow(self):
        print("Wow")


a1 = Animals("cat", "dog")
print(a1.animals1)

a1.wow()
