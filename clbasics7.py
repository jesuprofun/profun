
class Students:

    school = 'Geeks'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return ((self.m1 + self.m2 + self.m3) / 3)

    def get_m1(self):
        return self.m1

    def set_m1(self, value):
        self.m1 = value

    @classmethod
    def get_school(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is student class")


s1 = Students(34, 67, 32)
s2 = Students(89, 32, 12)

print(s1.avg())
print(s2.avg())

print(s1.get_m1())

s1.set_m1(48)
print(s1.get_m1())

print(Students.get_school())

print(Students.info())
