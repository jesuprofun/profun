
# def simple_generator():
#         yield 1
#         yield 2
#         yield 3

# x = simple_generator()



# print(next(x))
# print(next(x))
# print(next(x))

# for value in simple_generator():
#     print(next(x))

class Employee:
    hike = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    def full_name(self):
        return self.first + self.last
    
    def increment(self):
        self.pay = self.pay * Employee.hike
        return int(self.pay)

    @classmethod
    def set_increment(cls, amount):
        cls.hike = amount

    @staticmethod
    def company_name():
        return 'xyz'

    def __add__(self, other):
        return self.pay + other.pay
    
e1 = Employee('jesu', 'profun', 30000)
e2 = Employee('deva', 'steffina', 60000)
# print(e1.full_name())
# print(e1.increment())

# Employee.set_increment(1.06)
# print(e1.increment())

print(e1.company_name())

print(e1 + e2)