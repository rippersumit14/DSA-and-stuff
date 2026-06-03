#push method in the stack using the linkedlist
#in linkedlist implemented stack we always add in the start of the linked list
#it becomes more efficient

#declaring the node class
class Node:
    def __init__(self, value):
        self.value = value

#decalring the stack class
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = value
        self.length = 0

    #Decalring the push method
    #top of the element
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1

    #time-complexity-o(1)
    #space-complexity-o(1)
    

