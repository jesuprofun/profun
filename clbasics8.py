
class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def show(self):
        print(self.name, self.rollno)


s1 = Student('Profun', 2)
s2 = Student('Steffy', 3)

print(s1.show())
