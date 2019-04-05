
class Computer:
    def __init__(self):
        self.name = "Profun"
        self.age = 29

    def update(self):
        self.name = "Caisey"
        self.age = 4

    def compare(self,c2):
        if self.age == c2.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()

c2.name = "Steffy"
c1.age = 30

# c1.update()

if c1.compare(c2):
    print("They are same")
else:
    print("They are not same")
print(c1.name)
print(c2.name)

print(c1.age)
print(c2.age )