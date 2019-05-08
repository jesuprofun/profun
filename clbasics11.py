

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    def full_name(self):
        return '{} {}'.format(self.first,self.last)

    def hike(self):
        self.pay = int(self.pay * Employee.increment)

    def __repr__(self):
        pass

    def __str__(self):
        pass


emp_1 = Employee('Jesu', 'Profun', 20000)
emp_2 = Employee('Deva', 'Steffina', 30000)

print(emp_1)

repr(emp_1)
str(emp_1)