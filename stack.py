
class Stack:

    def __init__(self, container, stack_size):
        self.container = []
        self.stack_size = stack_size

    def push(self, container):
        if len(self.container) < self.stack_size:
            self.container.append(container)
        else:
            raise Exception("Container is full")

    def pop(self):
        if len(self.container) == 0:
            raise Exception("Container is Empty")
        else:
            return self.container.pop()

    def display(self):
        print(self.container)


if __name__ == '__main__':

    c1 = Stack(None, 4)

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
