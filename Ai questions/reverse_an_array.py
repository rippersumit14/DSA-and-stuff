#in this we have to reverse the array

import numpy as np

arr1 = np.array([[1,2,3,4],[5,6,7,8], [11,12,13,14]])

def reverse_array(array):
    arr3 = np.zeros((3,4))#creates the array of fixed size
    target = 0
    for i in range(len(array) -1, -1, -1):
        arr3[target] = array[i]
        target += 1

    return arr3

print(reverse_array(arr1))

#the time complexity will be o(mn)
#the space complexity will be o(mn)


