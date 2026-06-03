#in this we will use the get method in which we will pass the index as the parameter

#defining the node class
class Node:
    def __init__(self, value): #declaring the value and next address
        self.value = value
        self.next = None

#defining the linkedlist class
class LinkedList:
    def __init__(self):
            self.head = None
            self.tail = None
            self.length = 0

            # printing the linked list

    def __str__(self):
        temp = self.head
        result = ""

        while temp:
            result += str(temp.value)

            if temp.next:
                result += " -> "

            temp = temp.next  # IMPORTANT: move to next node

        return result

    #creating for end of the linkedlist
    def append(self, value):
        new_node = Node(value)

        # check if linked list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    #declaring the new method for the insertion of the element using the insert method
    def insert(self, index, value):
        new_node = Node(value)
        temp_node = self.head
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

    #creating the traversal method for the traversal of the linked list
    def traversal(self):
        current = self.head #starts from the head of the linked list which will be the first element
        while current is not None:
            print(current.value)
            current = current.next

    #creating the get method
    def get(self, index):  #passing index as the parameter
        if index == -1:
            return self.tail
        current = self.head
        for _ in  range(index):
            current = current.next
        return current.value








newlinkedlist = LinkedList()

newlinkedlist.append(1)
newlinkedlist.append(2)
newlinkedlist.append(3)
newlinkedlist.append(4)
newlinkedlist.append(5)
newlinkedlist.append(6)

print(newlinkedlist.get(2))



#the time complexity will be o(n)
#the space complexity will be o(1)






