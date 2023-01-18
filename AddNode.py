class Node:
    def __init__(self, dataval=None):
        self.prev = None
        self.next = None
        self.val = dataval


class LinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def add(self, val):
        node = Node(val)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.head
            self.tail = self.tail
            self.size += 1

    def __str__(self):
        vals = []
        node = self.head
        while node is not None:
            vals.append(node.val)
            node = node.next
        return f"[{', '.join(str(val) for val in vals)}]"


my_list = LinkedList()
my_list.add(4)
my_list.add(45)
print(my_list)
