# ==============================
# NODE CLASS
# ==============================

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# ==============================
# STACK CLASS USING LINKED LIST
# ==============================

class Stack:

    # Constructor
    def __init__(self, value):

        # Create first node
        new_node = Node(value)

        # Top points to newest node
        self.top = new_node

        # Current size of stack
        self.length = 1


    # ==============================
    # PUSH OPERATION
    # Adds element to top
    # ==============================
    def push(self, value):

        # Create new node
        new_node = Node(value)

        # New node points to current top
        new_node.next = self.top

        # Move top to new node
        self.top = new_node

        # Increase stack size
        self.length += 1


    # ==============================
    # POP OPERATION
    # Removes top element
    # ==============================
    def pop(self):

        # Check if stack is empty
        if self.top is None:
            return None

        # Store current top node
        popped_node = self.top

        # Move top to next node
        self.top = self.top.next

        # Disconnect popped node
        popped_node.next = None

        # Reduce length
        self.length -= 1

        # Return removed value
        return popped_node.value


    # ==============================
    # PEEK OPERATION
    # Returns top value
    # ==============================
    def peek(self):

        if self.top is None:
            return None

        return self.top.value


    # ==============================
    # DISPLAY STACK
    # ==============================
    def display(self):

        temp = self.top

        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next

        print("None")


# ==============================
# DRIVER CODE
# ==============================

my_stack = Stack(1)

my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

# Stack:
# 30 -> 20 -> 10 -> 1 -> None

print("Top Element:", my_stack.top.value)

print("Popped Element:", my_stack.pop())

print("Current Stack:")
my_stack.display()

print("Stack Length:", my_stack.length)