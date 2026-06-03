# Node class represents each element in the list
class Node:
    def __init__(self, value):
        self.value = value   # store the actual value
        self.next = None     # pointer to next node


# Circular Singly Linked List class
class CSLinkedList:
    def __init__(self, value):
        newNode = Node(value)

        # Initially, head and tail both point to the same node
        self.head = newNode
        self.tail = newNode

        # Circular condition → node points to itself
        newNode.next = newNode

        # Length of list
        self.length = 1


    # Append method → add node at the end
    def append(self, value):
        newNode = Node(value) #created the new node

        # Case 1: If list is empty
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode   # circular link

        # Case 2: Normal case
        else:
            self.tail.next = newNode   # old tail points to new node
            newNode.next = self.head  # new node points to head (circular)
            self.tail = newNode       # update tail

        self.length += 1


    # Traverse (very important to avoid infinite loop)
    def traverse(self):
        if self.length == 0:
            return

        current = self.head

        while True:
            print(current.value)
            current = current.next

            if current == self.head:   # stop when full cycle completes
                break

csLinky = CSLinkedList(10)  # first node

csLinky.append(20)
csLinky.append(30)

csLinky.traverse()  # to see output

#The time-complexity of the code will be o(1)
#The space-complexity of the code will be o(1)

