from node import Node
#  inserir na pilha
#  remover da pilha
#  observar o topo da pilha
class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elem):
        #insere um elemento na pilha
        node = Node(elem)
        node.next = self.top
        self.top = node
    
    def pop(self):
        # remove o top da pilha
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size -= 1
            return node.data
        raise IndexError('The stack is empty')

    def peek(self):
        # retorna o topo sem remover
        if self._size > 0:
            return self.top.data
        raise IndexError('The stack is empty')

    def __len__(self):
        return self._size

    def __repr__(self):
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()



x = Stack()
x.push(2)
x.push(4)
x.push(32)
x.push(222)
x.push(True)
print(x)