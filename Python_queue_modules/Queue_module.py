#Collections module
#queue module
#MultiProcessing module

#collections module
from collections import deque

custom_queue = deque(maxlen=3) #can declare with size and also without size too
print(custom_queue)

custom_queue.append(1)
custom_queue.append(2)
custom_queue.append(3)

print(custom_queue.popleft()) #first element from the left side is removed

