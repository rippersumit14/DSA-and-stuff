#in this we have to find the minimum of the array
from array import *

arr1 = array("i", [11,22,33,44,55])

def minimum_element_of_the_array(arr):
    minimum_element = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < minimum_element:
            minimum_element = arr[i]

    return minimum_element

print(minimum_element_of_the_array(arr1))

#the time complexity of this code will be o(n)
#the space complexity will be o(1)