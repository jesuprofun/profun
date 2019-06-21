
class Indexing:

    def __init__(self, size):
        self.size = size
        self.map = self.size * []
        self.keys = []

    def put(self, keys, value):
        count = 0
        for key in keys:
            if key in self.keys:
                for i in self.map:
                    if i[0] == key:
                        if i[1][0] == value:
                            count += 1
                            i[1][1] = count
                        else:
                            pass


            else:

                key_value = [key, [value, 0]]
                self.map.append(key_value)

            self.keys.append(key)
        for i in self.map:
            print(i)
        # print(self.keys)



ind1 = Indexing(50)
with open('new_1.txt', 'r') as file1:
    keys1 = file1.read().strip().split()

with open('new_2.txt', 'r') as file1:
    keys2 = file1.read().strip().split()

keys = keys1 + keys2

ind1.put(keys, 'new_1.txt')
x