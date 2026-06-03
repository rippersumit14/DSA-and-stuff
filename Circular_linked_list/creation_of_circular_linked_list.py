#In this we will create the circular linked list

#defining the node class
class Node:
    def __init__(self, value):
        self.value = None
        self.next = None

class CSLinkedList:
    def __init__(self, value):
        NewNode = Node(value)
        NewNode.next = NewNode #points to itself
        NewNode.head = NewNode
        NewNode.tail = NewNode #as we have only one node
        NewNode.length = 1


csLinkedList = CSLinkedList(10)

print(csLinkedList)



