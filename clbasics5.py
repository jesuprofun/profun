class Computer:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer('Profun', 29)
c2 = Computer('Caisey', 4)

c1.name = "Steffina"

if c1.compare(c2):
    print("They are same")
else:
    print("They are not same")

print(c1.name)
print(c1.age)

print(c2.name)
print(c2.age)
