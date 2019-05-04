
class Person:
    name = "Profun"

    def __init__(self, name = None):
        self.name = name
    
profun = Person("Profun")
print("%s name is %s", Person.name, profun.name)

steffy = Person()
print("%s name is %s", Person.name, steffy.name)