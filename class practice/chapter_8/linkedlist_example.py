class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f"Node({self.value})"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def get_node(self, index):
        if index < 0 or index >= self.length:
            return None
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return current_node

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.value))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev_node = self.get_node(index - 1)
            new_node.next = prev_node.next
            prev_node.next = new_node
        self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
        else:
            prev_node = self.get_node(index - 1)
            prev_node.next = prev_node.next.next
        self.length -= 1