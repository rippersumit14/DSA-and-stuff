#insertion in linked list adding a new node at a specified position

#front, mid, before a node, after a node, at a specific position, at the end of the linked list

#creating the node for the linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None #single element node

#creating the linked list class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

        # for printing the linkedlist __str__ method is used
        # in python it is a special type of string representation of an instance

    def __str__(self):
        temp_node = self.head  # created a temporary node and put the head of the original node
        result = ''  # the output empty basically
        while temp_node is not None:  # it means until we have reached the end of the linked list
            result += str(
                temp_node.value)  # until the temp_node is not empty till then keep adding the value in the result in the string format
            if temp_node is not None:
                result += '->'
            temp_node = temp_node.next  # if temp node is not none then add -> to it. accessed though the node class next
        return result

    #creting the append method for the insertion in the linked list
    def append(self, value):
        new_node = Node(value)
        #check if this linked list is empty or not
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1


newLinkedList = LinkedList()
newLinkedList.append(10)
newLinkedList.append(20)

print(newLinkedList.tail)
print(newLinkedList)



#printing and adding different classes workflow