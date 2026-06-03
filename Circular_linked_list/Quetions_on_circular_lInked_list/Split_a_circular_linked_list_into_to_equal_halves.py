'''
Split a Circular Linked List into Two Equal Halves
Write a function to split the circular linked list into two equal halves. If the list has odd number of nodes, the extra node should go to the first list.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:  # Stop condition for circular list
                break
            result += ' -> '
        return result

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def split_list(self):
            result = [] #created an empy array
            temp = self.head

            while True:
                result.append(temp.value)
                temp = temp.next
                if temp == self.head:
                    break

            count = 0

            for i in result:
                count += 1

            if count % 2 == 0:
                mid = count // 2
            else:
                mid = (count // 2) + 1

            #splitting the arrays into two parts
            first_part = result[:mid]
            second_part = result[mid:]

            first_list = CSLinkedList()
            second_list = CSLinkedList()

            for val in first_part:
                first_list.append(val)

            for val in second_part:
                second_list.append(val)

            return first_list, second_list #in the form of singly linked list

        # #optmized solution for the split a circular linked list
    def optimized_spilt(self):
        if self.head is None:
            return None, None #handling the edge case if no node is present

        if self.head.next == self.head:
            return self, None #handling the edge case if only one node is present

        #declaring the slow and the fast pointer
        slow = self.head #moves 1 step
        fast = self.head #moves 2 step

        #Finding the middle using slow and fast pointer
        while fast.next != self.head and fast.next.next != self.head:
            slow = slow.next
            fast = fast.next.next

        #handle even no. of nodes
        if fast.next.next == self.head:
            fast = fast.next




        #first half
        head1 = self.head

        #second half
        head2 = slow.next

        # Break the list into two circular lists
        slow.next = head1
        fast.next = head2

        # Create two new circular linked list object
        first_list = CSLinkedList()
        second_list = CSLinkedList()

        first_list.head = head1
        second_list.head = head2

        return  first_list, second_list

















