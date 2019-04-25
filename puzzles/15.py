from operator import itemgetter

lyst = []
while True:
    str_input = input("Enter name, age,score:")
    if not str_input:
        break
    lyst.append(tuple(str_input.split(',')))
print(lyst)
print(sorted(lyst, key =itemgetter(0, 1, 2)))