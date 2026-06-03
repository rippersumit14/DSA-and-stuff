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

    def __str__(self):
        temp_node = self.head
        #create a result variable for the final printing
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head: #If not put this condition then it will create the infinite loop
                break
            result += '->'

        return result

    #Append method → add node at the end
    def append(self, value):
        newNode = Node(value)

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

    #Search method -> if the element exist or not
    def search(self, target):
        current = self.head
        while current is not None:
            if current.value == target:
                return True
            current = current.next
            if current.next == self.head:
                break
        return False

#Time-complexity of this code will be o(n)



CsLinky = CSLinkedList(1)
CsLinky.append(2)
CsLinky.append(3)
CsLinky.append(4)

print(CsLinky.search(44))

print(CsLinky)






