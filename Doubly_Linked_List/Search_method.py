#search method
#Prepend Method=> Adding the node in the beginning
#newly created node next pointer will point to the head pointer
#head prev pointer will point to the newly created node
#newly created node prev pointer will point to None

#Append method-> Adds the node to the end of the doubly linked list
#We create the new node with next and prev pointer
#Then make the last node next pointer to new node
#Make the new node prev pointer to the prev node

#declaring the node class
class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value

#declaring the DoublyLinkedListClass
class DoublyLinkedList:
    def __init__(self, value):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += ' <-> '
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            newNode.prev = None
        self.length += 1

    #search method
    def search(self, target):
        current_node = self.head
        while current_node:
            if current_node.value == target:
                return True
            current_node = current_node.next
        return False


newDll = DoublyLinkedList(1)
newDll.append(1)
newDll.append(2)
newDll.append(3)

#prepend method
newDll.prepend(10)
newDll.prepend(20)



print(newDll)

#The time complexity will be o(n)
