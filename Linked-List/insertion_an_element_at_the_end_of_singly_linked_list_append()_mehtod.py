# insertion in linked list adding a new node at the end

# creating the node for the linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# creating the linked list class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    # append method for insertion at the end
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


    # printing the linked list
    def __str__(self):
        temp = self.head
        result = ""

        while temp:
            result += str(temp.value)

            if temp.next:
                result += " -> "

            temp = temp.next   # IMPORTANT: move to next node

        return result


# creating the linked list
newLinkedList = LinkedList()

# inserting values4
newLinkedList.append(10)
newLinkedList.append(20)
newLinkedList.append(40)


# printing linked list
print(newLinkedList)

# printing tail value
print("Tail value:", newLinkedList.tail.value)

# printing length
print("Length:", newLinkedList.length)