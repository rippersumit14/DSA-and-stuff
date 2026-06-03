#Insert method-> “Insert a new node at a specific position in the list.”

#set method-> set(index, value) means:“Go to a specific index and update the value of that node.”






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

    #Adding the traverse method
    def traverse(self):
        currrent_node = self.head
        while currrent_node:
            print(currrent_node.value)
            currrent_node = currrent_node.next
            if currrent_node == self.head:
                break

    #adding the reverse traverse method
    def reverse_traverse(self):
        current_node = self.tail
        while current_node:
            print(current_node.value)
            current_node = current_node.prev
            if current_node == self.tail:
                break

    def search(self, value):
        if self.length == 0:
            return "List is empty"

        current = self.head

        while True:
            # Check current node
            if current.value == value:
                return "The element is present"

            current = current.next

            # Stop when we reach head again
            if current == self.head:
                break

        return "The element is not in the list"

    def get(self, idx):
        # Index validation
        if idx < 0 or idx >= self.length:
            return None

        current = self.head

        # Move idx steps forward
        for _ in range(idx):
            current = current.next

        return current

    # ---------------------------------------------
    # Set Method (Update value at given index)
    # Time Complexity: O(n)
    # ---------------------------------------------
    def set(self, idx, value):
        # Step 1: Get the node at index
        node = self.get(idx)

        # Step 2: Check if node exists
        if node:
            node.value = value  # Update value
            return True  # Success

        # Step 3: Invalid index
        return False

    # ---------------------------------------------
    # Insert Method (Insert node at given index)
    # Time Complexity: O(n)
    # ---------------------------------------------
    def insert(self, idx, value):
        # Invalid index
        # idx can be equal to length because inserting at end is allowed
        if idx < 0 or idx > self.length:
            return False

        # Insert at beginning
        if idx == 0:
            self.prepend(value)
            return True

        # Insert at end
        if idx == self.length:
            self.append(value)
            return True

        # Insert in middle
        new_node = Node(value)

        # Get node before target index
        prev_node = self.get(idx - 1)

        # Node currently at target index
        next_node = prev_node.next

        # Connect new node with previous and next node
        new_node.prev = prev_node
        new_node.next = next_node

        # Connect previous and next node back to new node
        prev_node.next = new_node
        next_node.prev = new_node

        # Increase length
        self.length += 1

        return True




# ---------------------------------------------
# Testing the CDLL
# ---------------------------------------------
newCdll = CircularDoublyLinkedList(1)
newCdll.append(2)
newCdll.append(3)
newCdll.append(4)

print(newCdll)

#The time complexity will be o(n)
