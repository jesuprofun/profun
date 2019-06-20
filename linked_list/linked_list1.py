

class Node:

    def __init__(self, item, next = None):
        self.item = item
        self.next = None


class Linked_list:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            self.head.next = new_node
            