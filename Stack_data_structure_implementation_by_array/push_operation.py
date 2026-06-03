#pusing the element in the stack, inserting the element in the stack
#declaring the stack class



class Stack:
    def __init__(self):
        self.items = [] #empty stack

    #declaring the push class
    def push(self, element):
        self.items.append(element) #maintains the lifo(last in first out)




#calling the stack class through variable
my_stack = Stack()

#calling the push method with values
my_stack.push(10)
my_stack.push(20)

print(my_stack.items)

#time-complexity-o(1)
#space-complexity-o(1)

