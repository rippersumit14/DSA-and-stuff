#defining the node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

#declaring the linked list class
class DoublyLinkedList:
    def __init__(self, value):
        newdoublyLinkedlist = Node(value)
