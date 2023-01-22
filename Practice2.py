class Node:
    def __init__(self, dataVal):
        self.prev = None
        self.next = None
        self.val = dataVal


class My_list:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def add(self, val):
        node = Node(val)
        if self.tail is None:
            self.tail = node
            self.head = node
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1

    def __str__(self):
        vals = []
        node = self.head
        while node is not None:
            vals.append(node.val)
            node = node.next
        return f"[{', '.join(str(val) for val in vals)}]"


my_list=My_list();
my_list.add(34)
my_list.add(3344)
my_list.add(4)
print(my_list)
