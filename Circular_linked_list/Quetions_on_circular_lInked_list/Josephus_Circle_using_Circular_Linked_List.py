class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def count_nodes(self):
        if not self.head:
            return 0
        count = 1
        temp = self.head
        while temp.next != self.head:
            count += 1
            temp = temp.next
        return count

    def delete_node(self, key):
        if self.head.data == key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            if self.head == self.head.next:
                self.head = None
            else:
                cur.next = self.head.next
                self.head = cur.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next

    def josephus_circle(self, step):
        #handling the edge case
        if self.head is None:
            return "List is empty"

        if self.head.next == self.head:
            return "Last person left standing: "+ self.head.data

        #Intialize pointers
        current = self.head

        # Find last node (prev)
        prev = self.head
        while prev.next != self.head:
            prev = prev.next


        while current.next != current:

            for _ in range(1, step-1):
                prev = current
                current = current.next

            #delete current node
            prev.next = current.next

            #move the next node
            current = current.next



        return f"Last person left standing: {current.data}"
