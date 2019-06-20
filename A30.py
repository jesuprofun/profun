
class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print(self.cpu, self.ram)

    def compare(self, c2):
        if c1.ram == c2.ram:
            return True
        else:
            return False


c1 = Computer('i5', 8)
c2 = Computer('i5', 8)

print(c1.compare(c2))

c1.config()
c2.config()

