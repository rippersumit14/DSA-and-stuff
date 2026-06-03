# set method will be used to update the value of any given node based on its index

# defining the node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# defining the linked list class
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

            temp = temp.next

        return result


    # append at end
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1


    # insert at index
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


    # traversal
    def traversal(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next


    # get node by index
    def get(self, index):

        if index < 0 or index >= self.length:
            return None

        current = self.head

        for _ in range(index):
            current = current.next

        return current   # RETURN NODE NOT VALUE


    # set value at index
    def set(self, index, value):

        temp_node = self.get(index)

        if temp_node:
            temp_node.value = value
            return True

        return False



# Creating linked list
newlinkedlist = LinkedList()

newlinkedlist.append(1)
newlinkedlist.append(2)
newlinkedlist.append(3)
newlinkedlist.append(4)
newlinkedlist.append(5)
newlinkedlist.append(6)

# updating value at index 2
newlinkedlist.set(2, 40)

print(newlinkedlist)