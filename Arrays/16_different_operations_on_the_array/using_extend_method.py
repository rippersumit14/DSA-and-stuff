#in this we have to extend python array using extend() method

from array import *

arr1 = array("i", [1,2,3,4,5])
arr2 = array("i", [1,2])

arr1.extend(arr2)

print(arr1)

#the time complexity of this code will be o(n)
#the space complexity of this code will be o(1)

