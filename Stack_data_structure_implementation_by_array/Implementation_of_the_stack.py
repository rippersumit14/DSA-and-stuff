#stack is a data structure that follows the LIFO method
#stack is implemented by arrays and linked list

#while declaring the stack using the array, we should always try to avoid choosing the front because adding in the front will cause the o(n) time complexity
#always focusing on the end of the list, time complexity-> o(n). More efficient

#creating the stack constructor
class Stack:
    def __init__(self):
        self.items = []#creating the empty stack


my_stack = Stack()
print(my_stack) #object
print(my_stack.items)#actual elements
#o(1)-> time complexity


