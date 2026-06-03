#Prepend method in cdll -> adds the element in the front of the list

# -------------------------------
# Node Class (Basic building block)
# -------------------------------
class Node:
    def __init__(self, value):
        self.value = value      # FIX: store actual value
        self.next = None        # pointer to next node
        self.prev = None        # pointer to previous node


# ---------------------------------------------
# Circular Doubly Linked List Class (CDLL)
# ---------------------------------------------
class CircularDoublyLinkedList:
    def __init__(self, value):
        # Create first node
        new_node = Node(value)

        # Head and Tail both point to same node initially
        self.head = new_node
        self.tail = new_node
        self.length = 1

        # Circular linking (points to itself)
        new_node.next = new_node
        new_node.prev = new_node


    # ---------------------------------------------
    # Append Method (Insert at end)
    # Time Complexity: O(1)
    # ---------------------------------------------
    def append(self, value):
        new_node = Node(value)

        # Link new node with tail
        new_node.prev = self.tail
        new_node.next = self.head

        # Fix existing links
        self.tail.next = new_node
        self.head.prev = new_node

        # Move tail pointer
        self.tail = new_node

        # Increase length
        self.length += 1


    # ---------------------------------------------
    # String Method (Print CDLL)
    # ---------------------------------------------
    def __str__(self):
        if self.length == 0:
            return "Empty List"

        current_node = self.head
        result = ""

        while True:
            result += str(current_node.value)
            current_node = current_node.next

            # Stop when we reach head again
            if current_node == self.head:
                break

            result += " <-> "

        return result

    #adding the perpend method
    def prepend(self, value):
        pre_New_node = Node(value)
        pre_New_node.next = self.head
        self.head.prev = pre_New_node
        self.tail.next = pre_New_node
        pre_New_node.prev = self.tail
        self.head = pre_New_node
        self.length += 1


# ---------------------------------------------
# Testing the CDLL
# ---------------------------------------------
newCdll = CircularDoublyLinkedList(1)
newCdll.append(2)
newCdll.append(3)
newCdll.append(4)

print(newCdll)

#The time complexity will be o(n)
#The space complexity will be o(1)
