class Node:
    def __init__(self, dataValue):
        self.prev = None
        self.next = None
        self.val = dataValue


class My_List:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def add(self, dataVal):
        node = Node(dataVal)
        if self.tail is None:
            self.head = node
            self.tail = node
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


listdb = My_List();
listdb.add(34)
listdb.add(234)
print(listdb)
