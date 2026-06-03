#in this we have to find the maximum element

from array import *

arr1= array("i", [1,2,3,4,5,1,2,3])

max_element = arr1[0]

for i in arr1:
    if i > max_element:
        max_element = i

print(max_element)

#the time complexity will be o(n) linear time
#the space complexity will be o(1) constant space

