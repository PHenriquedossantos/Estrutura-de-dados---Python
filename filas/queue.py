from node import Node

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0


    def push(self, elem):
        node = Node(elem)
        if self.last is None:
            ...        
    
    def pop(self):
        pass

    def peek(self):
        pass

    def __len__(self):
        return self._size

    def __repr__(self):
        pass

    def __str__(self):
        pass





