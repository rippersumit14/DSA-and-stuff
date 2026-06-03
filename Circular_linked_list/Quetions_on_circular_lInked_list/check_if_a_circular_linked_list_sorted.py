from wsgiref.validate import header_re


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def print_list(self):
        nodes = []
        temp = self.head
        while temp:
            nodes.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        print(" -> ".join(nodes))

    def is_sorted(self):
        #handle edge case
        if self.head is None:
            return True #empty list is considered sorted

        if self.head.next == self.head:
            return True

        #Intialize variables
        current = self.head
        drop_count = 0

        while True: #run this loop forever until  manually stop it
            if current.value > current.next.value:
                drop_count += 1

            current = current.next

            if current == self.head:
                break

        #final decision
        if drop_count <= 1:
            return True
        else:
            return False
