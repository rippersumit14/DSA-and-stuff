
# =========================================================
# CIRCULAR QUEUE USING LINKED LIST
# =========================================================

# ---------------------------------------------------------
# TIME COMPLEXITIES
# ---------------------------------------------------------
# Enqueue   -> O(1)
# Dequeue   -> O(1)
# Peek      -> O(1)
# isEmpty   -> O(1)
# isFull    -> O(1)
# Display   -> O(n)
#
# ---------------------------------------------------------
# SPACE COMPLEXITY
# ---------------------------------------------------------
# O(n)
# because we are storing n nodes in linked list
# =========================================================


# ---------------------------------------------------------
# NODE CLASS
# ---------------------------------------------------------
# Each node contains:
# data  -> actual value
# next  -> pointer to next node
# ---------------------------------------------------------

class Node:

    def __init__(self, data):

        self.data = data
        self.next = None


# =========================================================
# CIRCULAR QUEUE CLASS
# =========================================================

class CircularQueue:

    # -----------------------------------------------------
    # Constructor
    # -----------------------------------------------------
    def __init__(self, size):

        self.front = None
        self.rear = None

        # maximum size of queue
        self.size = size

        # current elements count
        self.count = 0


    # =====================================================
    # CHECK IF QUEUE IS EMPTY
    # =====================================================
    def isEmpty(self):

        return self.count == 0


    # =====================================================
    # CHECK IF QUEUE IS FULL
    # =====================================================
    def isFull(self):

        return self.count == self.size


    # =====================================================
    # ENQUEUE OPERATION
    # =====================================================
    # Insert element at REAR
    #
    # Logic:
    # 1. Create new node
    # 2. If queue empty:
    #       front = rear = new node
    #       rear.next points to front
    #
    # 3. Else:
    #       rear.next = new node
    #       rear = new node
    #       rear.next = front
    # =====================================================

    def enqueue(self, data):

        # Queue full
        if self.isFull():

            print("Queue is Full")
            return

        new_node = Node(data)

        # First element insertion
        if self.isEmpty():

            self.front = new_node
            self.rear = new_node

            # circular connection
            self.rear.next = self.front

        else:

            self.rear.next = new_node
            self.rear = new_node

            # circular link
            self.rear.next = self.front

        self.count += 1

        print(data, "inserted")


    # =====================================================
    # DEQUEUE OPERATION
    # =====================================================
    # Remove element from FRONT
    #
    # Logic:
    # 1. If empty -> return
    #
    # 2. If only one node:
    #       front = rear = None
    #
    # 3. Else:
    #       front moves forward
    #       rear.next updated to new front
    # =====================================================

    def dequeue(self):

        # Queue empty
        if self.isEmpty():

            print("Queue is Empty")
            return

        removed = self.front.data

        # Only one node present
        if self.front == self.rear:

            self.front = None
            self.rear = None

        else:

            self.front = self.front.next

            # maintain circular connection
            self.rear.next = self.front

        self.count -= 1

        print(removed, "removed")


    # =====================================================
    # PEEK OPERATION
    # =====================================================
    # Return front element
    # =====================================================

    def peek(self):

        if self.isEmpty():

            print("Queue is Empty")
            return

        print("Front Element:", self.front.data)


    # =====================================================
    # DISPLAY QUEUE
    # =====================================================
    # Traverse until we again reach front
    # =====================================================

    def display(self):

        if self.isEmpty():

            print("Queue is Empty")
            return

        temp = self.front

        print("Queue Elements:")

        while True:

            print(temp.data, end=" -> ")

            temp = temp.next

            # stop when full circle completed
            if temp == self.front:
                break

        print("(Back to Front)")


# =========================================================
# DRIVER CODE
# =========================================================

cq = CircularQueue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)

cq.display()

cq.peek()

cq.dequeue()

cq.display()

print("Is Queue Empty?", cq.isEmpty())

print("Is Queue Full?", cq.isFull())

cq.enqueue(40)
cq.enqueue(50)
cq.enqueue(60)

cq.display()

print("Is Queue Full?", cq.isFull())