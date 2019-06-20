
class Employee:
    
    hike = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    @property
    def full_name(self):
        return self.first + self.last

    def __add__(self, other):
        return self.pay + other.pay
    
    def increment(self):
        self.pay = int(self.pay * Employee.hike)
        return self.pay

    @classmethod
    def set_hike(cls, amount):
        cls.hike = amount

    @staticmethod
    def company_name():
        return 'xyz'
    

class Developer(Employee):
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    
dev1 = Developer('Jesu', 'Profun', 30000, 'Python')
dev2 = Developer('Deva', 'Steffina', 60000, 'Java')

print(dev1.prog_lang)
