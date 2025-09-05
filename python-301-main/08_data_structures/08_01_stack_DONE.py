# Build a custom `Stack` similar to the `Queue` you built

def depop_with_logging(func):
    def wrapper(self):
        print(f"Getting book... Current queue size: {self.length}")
        item = func(self)
        print(f"Got item: {item}. Updated queue size: {self.length}")
        return item
    return wrapper

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Stack:
    '''FIFO: First in first out
    - Basic 4 methods:
        - Push: adds an element to the collection
        - Pop: removes the most recently added element from the collection
        - Empty: checks whether there are any elements in the stack
        - Peek: returns the topmost element without removing it from the stack
    '''
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    
    def is_empty(self):
        return self.bottom is None

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.top.value
    
    def push(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1
    
    @depop_with_logging
    def pop(self):
        if self.is_empty():
            return None
        else:
            poped_node = self.top
            self.top = self.top.next
            self.length -= 1
            if self.is_empty():
                self.bottom = None
            return poped_node.value

books_stack = Stack()
books_stack.push("Book Python Crash Course by Eric Matthes")
books_stack.push("Book Automate the Boring Stuff with Python by Al Sweigart")
books_stack.push("Book Head First Python by Paul Barry")
books_stack.push("Book Fluent Python by Luciano Ramalho")
books_stack.push("Book Python Cookbook by David Beazley & Brian K. Jones")

# pop and see the decorated logging output
print("Lets read all 5 staked books from top to bottom!\n")

book = books_stack.pop() 
print(f"To read: {book}\n")  

book2 = books_stack.pop() 
print(f"To read: {book2}\n")  

book3 = books_stack.pop() 
print(f"To read: {book3}\n")  

book4 = books_stack.pop() 
print(f"To read: {book4}\n")  

book5 = books_stack.pop() 
print(f"To read: {book5}\n") 
