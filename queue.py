
class Queue:

    def __init__(self, container):
        self.container = []

    def push(self, container):
        self.container.append(container)

    def out(self):
        return self.container. pop(0)

q1 = Queue(None)

while True:
    choice = int(input("1. Enter number to the list\n2. Queue process\n3. Exit\nEnter your choice: "))
    if choice == 1:
        numbers = int(input("Enter the numbers: "))
        q1.push(numbers)
        print(q1.container)

    elif choice == 2:
        print("The first number {} is moved out".format(q1.out()))
        print("The container becomes ", q1.container)

    elif choice == 3:
        break

print(q1.container)
