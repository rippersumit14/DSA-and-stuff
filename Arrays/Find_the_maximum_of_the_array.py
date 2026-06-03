#in this we have to find the maximum of the array

from array import array

arr1 = array("i", [12, 3, 22, 1, 2])

def maximum_element_of_array(arr):
    max_element = arr[0]   # safest initialization

    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]

    return max_element

print(maximum_element_of_array(arr1))

#time complexity of this code will be o(n)
#space complexity of this code will be o(1)