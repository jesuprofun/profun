
class stack:

    def __init__(self, container):
        self.container = []

    def push(self, value):
        self.container.append(value)

    def pop(self):
        if self.container == []:
            return None
        else:
            return self.container.pop()

    def display(self):
        print(self.container)


s1 = stack(None)

numbers = [2,2,3,3,4,5,6,7,8,9,2,3]
ecount = 0
ocount = 0
for i in numbers:
    if i % 2 == 0:
        s1.push(i)
        ecount += 1
    else:
        s1.pop()
        ocount += 1

print(s1.container)
print("Even count = ", ecount)
print("Odd count = ", ocount)
