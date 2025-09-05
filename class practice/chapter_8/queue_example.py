def dequeue_with_logging(func):
    def wrapper(self):
        print(f"Getting item... Current queue size: {self.length}")
        item = func(self)
        print(f"Got item: {item}. Updated queue size: {self.length}")
        return item
    return wrapper

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.value
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    @dequeue_with_logging
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            dequeued_node = self.head
            self.head = self.head.next
            self.length -= 1
            if self.is_empty():
                self.tail = None
            return dequeued_node.value



morning_tasks = Queue()
morning_tasks.enqueue("get dressed")
morning_tasks.enqueue("eat breakfast")
morning_tasks.enqueue("go to work")

# Dequeue and see the decorated logging output
task = morning_tasks.dequeue() 
# OUTPUT:
# Getting item... Current queue size: 3
# Got item: get dressed. Updated queue size: 2

print(f"Todo: {task}")  # Todo: get dressed
