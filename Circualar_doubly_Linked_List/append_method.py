#append method in cdll-> adding in the end of the linked list
#Creating the circular Linked list

#creating the node class
class Node:
    def __init__(self, value):
        self.value = None
        self.next = None
        self.prev = None

    def __str__(self):

        return  str(self.value)


#Declaring the Circular_doubly_linked_list class
class CircularDoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        new_node.next = new_node
        new_node.prev = new_node
        #single node only

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        new_node.prev = self.tail
        new_node.next = self.head
        self.head.prev = new_node
        self.tail = new_node
        self.length += 1

newCdll = CircularDoublyLinkedList()
print(newCdll)

#The time complexity of this operation will be o(1)
#the space complexity of this operation will be o(n)

