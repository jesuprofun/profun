
class Hashmap:

    def __init__(self, size):
        self.size = size
        self.lyst = self.size * [None]

    def get_hashcode(self, code):
        length = len(code)
        return length % self.size

    def add_key(self, key, value):

        hash_code = self.get_hashcode(key)
        key_value = [key, value]

        if self.lyst[hash_code] is None:
            self.lyst[hash_code] = list(key_value)

        else:
            for pair in self.lyst[hash_code]:
                if pair[0] == key:
                    pair[1] = value
                
            self.lyst[hash_code].append(key_value)

        print(self.lyst)




h1 = Hashmap(5)
h1.add_key('Profun', 'Jesu')
h1.add_key("Prabhu", 'Hi')
h1.add_key("Lakshmi", 'Narayanan')
