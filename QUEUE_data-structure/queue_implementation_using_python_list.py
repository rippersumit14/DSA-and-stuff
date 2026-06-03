#queue can be implemented using the two ways
#Arrays and Linked lists

#Lists are slow in the concept of queue
#not that much efficient
#shifting problem

#enque and dequeue is used to remove and insert

#Create queue using python list and empty python list
#cannot insert in between
#always insert in the end of the queue

#creating the python queue without size
class Queue:
    def __init__(self):
        self.items = [] #empty list

    #str method -> for printing the queue
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values) #o(1) space and time complexity

    #isEmpty method
    def is_Empty(self):
        if self.items == []:
            return True
        else:
            return False #o(1) time complexity

    #Enqueue method
    def enqueue(self, value):
        self.items.append(value)
        return  "The element is inserted in the end of the queue" #-> the time complexity->o(n^2) and the space complexity will take the o(1)
    #Dequeue method -> Remove the first element
    def dequeue(self):
        if self.is_Empty():
            return "No element"
        else:
            return self.items.pop(0) #takes out the first element from the queue and the tc will be o(n) and sc will be o(1)
    #peek method-> returns the first element of the queue
    def peek(self):
        return self.items[0] #the time complexity will be o(1)

    #delete method
    def delete(self):
        self.items = None #all items are deleted
        #o(1) -> both space and time



custome_queue = Queue()
print(custome_queue.is_Empty())
custome_queue.enqueue(10)
custome_queue.enqueue(20)
custome_queue.enqueue(30)
custome_queue.enqueue(40)

custome_queue.dequeue()

print(custome_queue)



