#search in array can be performed by the linear search method
#Linear search-> The linear search algo performs the search ina array one by one, comparing each element with the target value

from array import *

arr1 = array("i", [1,2,3,4,5])

#creating the function for that
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return - 1

print(linear_search(arr1, 5)) #5 is located at the index 4

#time complexity for this code will be o(n)
#space complexity for this code will be o(1)

