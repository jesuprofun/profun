
class Employee:

    no_of_emps = 0
    increment = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

        Employee.no_of_emps += 1

    def full_name(self):
        return '{} {}'.format(self.first,self.last)

    def hike(self):
        self.pay = int(self.pay * Employee.increment)

    @classmethod
    def set_increment(cls, amount):
        cls.increment = amount

    @classmethod
    def from_string(cls, new_string):
        first, last, pay = new_string.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday -- 6:
            return False
        return True


emp_1 = Employee('Jesu', 'Profun', 20000)
emp_2 = Employee('Deva', 'Steffina', 30000)

print('Name = {} {}'. format(emp_1.first, emp_1.last), '\nPay = ', emp_1.pay, '\nEmail = ', emp_1.email)
print('\nName = ', emp_2.full_name(), '\nPay = ', emp_2.pay, '\nEmail = ', emp_2.email)

print('\nFull Name', emp_1.full_name())
print('Full Name', emp_2.full_name())

print('\nPay', emp_1.pay)
print('Pay', emp_2.pay)

emp_1.hike()
emp_2.hike()

print('\nPay raised', emp_1.pay)
print('Pay raised', emp_2.pay)

print('Total number of employees:', Employee.no_of_emps)

print(emp_1.increment)
print(emp_2.increment)

# emp_1.increment = 1.05
#
# print(emp_1.increment)
# print(emp_2.increment

Employee.set_increment(1.05)

print(emp_1.increment)
print(emp_2.increment)

new_str1 = 'Caisey-Rona-40000'
new_str2 = 'Chrisy-Riana-50000'

new_emp1 = Employee.from_string(new_str1)

print("New Employee mail is: ", new_emp1.email)
