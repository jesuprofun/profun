class Squares:

    def __init__(self, length):
        self.length = length
        self.i = 0 

    def __next__(self):
        print("Inside the next")
        self.i += 1
        if self.i >= self.length:
            raise StopIteration
        return self.i * 2
    
    def __iter__(self):
        print("Inside iterator")
        return self

    def __getitem__(self, index):
        print("Inside the getitem")
        self.i +=  1
        return self.i**2
        # return next(self)

class Iterator:

    def __init__(self, length):
        self.length = length
        self.i = 0
    
    def __next__(self):
        print("Inside the next")
        self.i += 1
        if self.i >= self.length:
            raise StopIteration
        return self.i * 2


s1 = Squares(6)
# for _ in range(20):
#     print(next(s1))

for i in s1:
    print(i)
