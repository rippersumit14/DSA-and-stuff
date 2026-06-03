#decalring the stack using a linked list
#push operation will add  beginning of the list and same for the pop

#end -> becomes of the time-complexity->o(n)
#beggining-> t-c-> o(1) #more efficient
#perform operations in the head

#declaring the node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node #head
        self.bottom = None #tail
        self.length = 0

new_stack = Stack()


#time-complexity->o(1)

#space-complexity->o(1)

