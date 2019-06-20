
class Table:

    def __init__(self, table):
        self.table = table
        self.i = 1
    
    def get_next_number(self):
        ans = self.i * self.table
        self.i += 1
        if self.i == 10:
            raise StopIteration
        return ans
        
    # def __iter__(self):
    #     return self
    
    # def __next__(self):
    #     self.i += 1
    #     if self.i >= 10:
    #         raise StopIteration
    #     return self.i * self.table



t = Table(4)
for _ in range(12):
    print(t.get_next_number())

# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))


# for i in t:
#     print(i)