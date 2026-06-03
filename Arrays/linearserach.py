#in this we have to perform linear search in an array

from array import *



arr1 = array("i", [1,2,3,43,5])

target = [0]


def Linear_search(array_name, target):
    for element in range(len(array_name)):
        if array_name[element] == target:
            return element
    return -1


print(Linear_search(arr1, 43))

#the time complexity will be o(n)
#the space complexity will be o(1)

