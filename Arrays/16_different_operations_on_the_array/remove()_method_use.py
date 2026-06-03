#in this we have to remove the array element using the remove() method

from array import *

arr1 = array("i",[1,2,3,4,5])
arr1.remove(3)

print(arr1)

#it can also be done by the pop method
arr1.pop(2)#this passes the index value
print(arr1)

