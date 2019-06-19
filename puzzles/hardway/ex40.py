
class Mystuff:
     
    def __init__(self):
        self.tangerine = "Something to be typed"
    
    @property
    def apple(self):
        print("I'm classy apples")


stuff = Mystuff()
print(stuff.tangerine)
stuff.apple