#now implementing the queue with a fixed capacity
class Queue:
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1
        #tc -> o(1), sc-> o(1)

    #str method
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    #full method
    def isFull(self):
        if self.top +  1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False #tc -> o(1)

    #isEmpty method
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False #tc -> o(1)

    #enque method
    def enqueue(self, value):
        if self.isFull():
            return "The queue is full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value #o(1) time compelxity

    #deque method
    def dequeu(self):
        firstElement = self.items[self.start]
        start = self.start
        if self.start == self.top: #only one element
            self.start = -1
            self.top = -1
        elif self.start + 1 == self.maxSize:
            self.start = 0
        else:
            self.start += 1
        self.items[start] = None
        return firstElement #o(1) time complexity






customCircularQueue = Queue(2)
customCircularQueue.enqueue(1)

customCircularQueue.enqueue(1)

customCircularQueue.enqueue(1)

customCircularQueue.enqueue(1)


print(customCircularQueue)

