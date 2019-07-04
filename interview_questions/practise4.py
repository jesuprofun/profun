
class A:
    def cat(self):
        print("In A")

class B():
    def cat(self):
        print("In B")

class C(A,B):
    def cat1(self):
        print("In C")


c = C()
c.cat()