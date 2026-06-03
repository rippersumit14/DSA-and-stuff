class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)

        self.head = new_node
        self.tail = new_node
        self.length = 1


    def __str__(self):
        temp_node = self.head
        result = ""

        while temp_node is not None:
            result += str(temp_node.value)

            if temp_node.next is not None:
                result += "->"

            temp_node = temp_node.next

        return result


newLinkedlist = LinkedList(10)

print(newLinkedlist)