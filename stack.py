
class stack:

    def __init__(self, container):
        self.container = []

    def push(self, container):
        self.container.append(container)

    def pop(self):
        return self.container.pop()

    def display(self):
        print(self.container)


if __name__ == '__main__':

    c1 = stack(None)

    while True:
        choice =int(input("1. Add numbers to the container\n2. Pop the number\n3. Display\n4. Exit\nEnter your choice"))
        if choice == 1:
            numbers = int(input("Enter the numbers: "))
            c1.push(numbers)
            print(c1.container)

        if choice == 2:
            print("The number {} is removed from the list".format(c1.pop()))
            print("The container becomes ", c1.container)

        if choice == 3:
            c1.display()

        if choice == 4:
            break


    print(c1.container)
