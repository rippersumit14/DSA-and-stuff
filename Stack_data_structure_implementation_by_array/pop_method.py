#taking out the elements from the stack
#declaring the stack class
class Stack:
    def __init__(self):
        self.items = []

    #decalring the push method
    def push(self, element):
        self.items.append(element)

    #declaring the is_empty method
    def is_empty(self):
        return len(self.items) == 0

    #declaring the str method
    def __str__(self):
        #edge case checking if the stack is empty using the is_empty stack method
        if self.is_empty():
            return "Stack is empty"
        values = [str(x) for x in reversed(self.items)]
        return '\n'.join(values)

    #declaring the pop method
    def pop(self):
        if self.is_empty(): #edge case
            return " stack is empty "
        return self.items.pop() #Time-complexity-o(1) and space-complexity->o(n)






#calling the stack class
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
my_stack.push(6)

my_stack.pop()#takes out the element

print(my_stack)
