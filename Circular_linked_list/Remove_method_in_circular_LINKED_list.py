# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Circular Singly Linked List
class CSLinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        newNode.next = newNode  # circular link
        self.length = 1

    def __str__(self):
        if self.head is None:
            return "Empty"

        temp = self.head
        result = ""

        while True:
            result += str(temp.value)
            temp = temp.next
            if temp == self.head:
                break
            result += " -> "

        return result

    # Append at end
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

    # Get node by index
    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        current = self.head
        for _ in range(index):
            current = current.next

        return current

    # Set value at index
    def set(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    # Remove first node
    def pop_first(self):
        if self.length == 0:
            return None

        popped = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped.next = None

        self.length -= 1
        return popped

    # Remove last node
    def pop(self):
        if self.length == 0:
            return None

        popped = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next

            temp.next = self.head
            self.tail = temp
            popped.next = None

        self.length -= 1
        return popped

    # Remove node by index
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        prev = self.get(index - 1)
        popped = prev.next
        prev.next = popped.next
        popped.next = None

        self.length -= 1
        return popped

    # Count nodes (best way)
    def count(self):
        return self.length


# ------------------ Testing ------------------

CsLinky = CSLinkedList(1)
CsLinky.append(2)
CsLinky.append(3)
CsLinky.append(4)

print("List:", CsLinky)
print("Count:", CsLinky.count())

CsLinky.pop_first()
print("After pop_first:", CsLinky)

CsLinky.pop()
print("After pop:", CsLinky)

CsLinky.remove(1)
print("After remove index 1:", CsLinky)

