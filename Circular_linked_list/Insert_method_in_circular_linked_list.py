# Node class represents each element in the list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Circular Singly Linked List class
class CSLinkedList:
    def __init__(self, value):
        newNode = Node(value)

        self.head = newNode
        self.tail = newNode

        newNode.next = newNode  # circular link
        self.length = 1

    # Print the list
    def __str__(self):
        if self.length == 0:
            return "Empty List"

        temp_node = self.head
        result = ''

        while True:
            result += str(temp_node.value)
            temp_node = temp_node.next

            if temp_node == self.head:
                break
            result += ' -> '

        return result

    # Append → insert at end
    def append(self, value):
        newNode = Node(value)

        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
        else:
            self.tail.next = newNode
            newNode.next = self.head
            self.tail = newNode

        self.length += 1

    # Prepend → insert at beginning
    def prepend(self, value):
        newNode = Node(value)

        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
        else:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = self.head  # maintain circular link

        self.length += 1

    # Insert at specific index
    def insert(self, index, value):
        # Edge cases
        if index < 0 or index > self.length: #if invalid index then prints the invalid index and all
            return "Invalid Index"

        if index == 0:
            self.prepend(value) #if the index == 0 then add in the front
            return

        if index == self.length: #if the index is the last element then use the append function
            self.append(value)
            return

        newNode = Node(value)
        temp_node = self.head

        # go to node before index
        for _ in range(index - 1):
            temp_node = temp_node.next

        newNode.next = temp_node.next
        temp_node.next = newNode

        self.length += 1

    # Traverse (for learning)
    def traverse(self):
        if self.length == 0:
            return

        current = self.head
        while True:
            print(current.value)
            current = current.next

            if current == self.head:
                break


# ------------------ TESTING ------------------

CsLinky = CSLinkedList(1)

CsLinky.append(2)
CsLinky.append(3)
CsLinky.append(4)

CsLinky.prepend(20)

CsLinky.insert(2, 34)

print(CsLinky)