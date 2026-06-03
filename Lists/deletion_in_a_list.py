#in this we will have the deletion from a list
from os import remove

list1 = [1,2,3,4,5,6]

#we will use the slice method
print(list1[1:])

#lists methods are pop,delete and remove

list1.pop(1) #declare the index as the parameter
print(list1)

list1.remove(6) #takes the current element/item value as the parameter
print(list1)



