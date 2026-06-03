#peek method -> it simply returns the last added element in the stack
#defining the stack class
class Stack:
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)

    #adding the is_empty_method
    def is_empty(self):
        return len(self.items) == 0

    #decalring the str method for the
    def __str__(self):
        if self.is_empty():
            return "Stack is empty"
        values = [str(x) for x in reversed(self.items)]
        return '\n'.join(values)

    #declaring the pop method
    def pop(self):
        return self.items.pop()

    #declaring the peek method
    def peek(self):
        return self.items[-1]

    #decalring the size method
    def size(self):
        return len(self.items)

    #declaring the clear method
    def clear(self):
        self.items = []

#time-complexity->o(1)
#space-complexity->o(1)