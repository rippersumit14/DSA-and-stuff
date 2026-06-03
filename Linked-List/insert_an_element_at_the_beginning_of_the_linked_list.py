# Insert element at the beginning of a singly linked list

# -------------------------------
# Defining the Node class
# -------------------------------
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # Pointer to the next node


# -------------------------------
# Defining the LinkedList class
# -------------------------------
class LinkedList:
    def __init__(self):
        # Initially, the linked list is empty
        self.head = None
        self.tail = None
        self.length = 0

    # ---------------------------------
    # __str__ method to print the list
    # ---------------------------------
    def __str__(self):
        temp_node = self.head
        result = ""

        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:  # Add arrow only if next node exists
                result += " -> "
            temp_node = temp_node.next

        return result

    # ---------------------------------
    # Prepend method (Insert at beginning)
    # ---------------------------------
    def prepend(self, value):
        new_node = Node(value)

        # If the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # Point new node to current head
            new_node.next = self.head
            # Move head to new node
            self.head = new_node

        self.length += 1


# -------------------------------
# Using the Linked List
# -------------------------------
linked_list_1 = LinkedList()

linked_list_1.prepend(10)
linked_list_1.prepend(20)
linked_list_1.prepend(30)
linked_list_1.prepend(40)
linked_list_1.prepend(50)

print(linked_list_1)