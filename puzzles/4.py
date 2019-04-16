
class Strings:

    def __init__(self):
        self.str = ""

    def get_string(self):
        self.str = input("Enter a string: ")

    def print_string(self):
        print(self.str.upper())

s1 = Strings()

s1.get_string()
s1.print_string()
