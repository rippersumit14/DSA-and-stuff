#array traversing
import array

from array import *

arr1 = array("i", [1,2,3,4,5])
arr2 = array("i", [1,43,5,32,1])

def traverseArray(array):
    for i in array:
        print(i)

print(traverseArray(arr1))

#time complexity will be o(n)
#space complexity will be o(1)








